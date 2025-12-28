#!/bin/bash
# OpenCode Configuration Installer
# Installs agents and skills with automatic backup

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OPENCODE_CONFIG_DIR="$HOME/.config/opencode"
BACKUP_DIR="$HOME/.opencode-backups"
BACKUP_MAX_SIZE_MB=20
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

# Functions
log_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[OK]${NC} $1"
}

log_warning() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

create_backup() {
    local source_dir="$1"
    local backup_name="$2"
    
    if [ -d "$source_dir" ] && [ "$(ls -A "$source_dir" 2>/dev/null)" ]; then
        local backup_path="$BACKUP_DIR/$backup_name-$TIMESTAMP"
        mkdir -p "$backup_path"
        cp -r "$source_dir"/* "$backup_path/" 2>/dev/null || true
        log_success "Backup created: $backup_path"
        cleanup_backups
        return 0
    fi
    return 1
}

cleanup_backups() {
    # Clean up old backups if total size exceeds limit
    if [ ! -d "$BACKUP_DIR" ]; then
        return
    fi
    
    local max_size_kb=$((BACKUP_MAX_SIZE_MB * 1024))
    local current_size_kb=$(du -sk "$BACKUP_DIR" 2>/dev/null | cut -f1)
    
    if [ "$current_size_kb" -le "$max_size_kb" ]; then
        return
    fi
    
    log_info "Backup size (${current_size_kb}KB) exceeds limit (${max_size_kb}KB), cleaning up..."
    
    # Get list of backups sorted by date (oldest first)
    # Backup names are like: agents-20241228_134500, skills-20241228_134500
    local backups=($(ls -1 "$BACKUP_DIR" 2>/dev/null | sort))
    
    for backup in "${backups[@]}"; do
        if [ "$current_size_kb" -le "$max_size_kb" ]; then
            break
        fi
        
        local backup_path="$BACKUP_DIR/$backup"
        local backup_size_kb=$(du -sk "$backup_path" 2>/dev/null | cut -f1)
        
        rm -rf "$backup_path"
        current_size_kb=$((current_size_kb - backup_size_kb))
        log_info "Removed old backup: $backup (${backup_size_kb}KB freed)"
    done
    
    log_success "Cleanup complete. Current size: ${current_size_kb}KB"
}

show_diff() {
    local source="$1"
    local dest="$2"
    local name="$3"
    
    if [ -f "$dest" ]; then
        if ! diff -q "$source" "$dest" > /dev/null 2>&1; then
            log_warning "Changes detected in $name:"
            diff --color=auto -u "$dest" "$source" 2>/dev/null | head -20 || true
            echo ""
            return 0
        fi
    fi
    return 1
}

install_agents() {
    log_info "Installing agents..."
    
    local agent_dir="$OPENCODE_CONFIG_DIR/agent"
    mkdir -p "$agent_dir"
    
    # Backup existing agents (ignore if empty)
    create_backup "$agent_dir" "agents" || true
    
    # Install each agent
    for agent_file in "$SCRIPT_DIR/agents"/*.md; do
        if [ -f "$agent_file" ]; then
            local agent_name=$(basename "$agent_file")
            local dest="$agent_dir/$agent_name"
            
            if [ -f "$dest" ]; then
                if diff -q "$agent_file" "$dest" > /dev/null 2>&1; then
                    log_info "Agent $agent_name unchanged, skipping"
                    continue
                else
                    log_warning "Agent $agent_name will be updated"
                fi
            fi
            
            cp "$agent_file" "$dest"
            log_success "Installed: $agent_name"
        fi
    done
}

install_skills() {
    log_info "Installing skills..."
    
    local skill_dir="$OPENCODE_CONFIG_DIR/skill"
    mkdir -p "$skill_dir"
    
    # Backup existing skills (ignore if empty)
    create_backup "$skill_dir" "skills" || true
    
    # Install each skill (they're in subdirectories)
    for skill_subdir in "$SCRIPT_DIR/skills"/*; do
        if [ -d "$skill_subdir" ]; then
            local skill_name=$(basename "$skill_subdir")
            local dest_dir="$skill_dir/$skill_name"
            mkdir -p "$dest_dir"
            
            if [ -f "$skill_subdir/SKILL.md" ]; then
                local dest="$dest_dir/SKILL.md"
                
                if [ -f "$dest" ]; then
                    if diff -q "$skill_subdir/SKILL.md" "$dest" > /dev/null 2>&1; then
                        log_info "Skill $skill_name unchanged, skipping"
                        continue
                    else
                        log_warning "Skill $skill_name will be updated"
                    fi
                fi
                
                cp "$skill_subdir/SKILL.md" "$dest"
                log_success "Installed skill: $skill_name"
            fi
        fi
    done
}

install_rules() {
    log_info "Installing rules..."
    
    local source_file="$SCRIPT_DIR/AGENTS.md"
    local dest_file="$OPENCODE_CONFIG_DIR/AGENTS.md"
    
    if [ ! -f "$source_file" ]; then
        log_warning "No AGENTS.md found in repo, skipping"
        return 0
    fi
    
    if [ -f "$dest_file" ]; then
        if diff -q "$source_file" "$dest_file" > /dev/null 2>&1; then
            log_info "AGENTS.md unchanged, skipping"
            return 0
        else
            log_warning "AGENTS.md will be updated"
        fi
    fi
    
    cp "$source_file" "$dest_file"
    log_success "Installed AGENTS.md (global rules)"
}

install_mcp() {
    log_info "Configuring MCP servers..."
    
    local mcp_dir="$SCRIPT_DIR/mcp"
    
    if [ ! -d "$mcp_dir" ]; then
        log_warning "No MCP directory found, skipping"
        return 0
    fi
    
    # Configure notify server
    if [ -f "$mcp_dir/notify/configure.py" ]; then
        if python3 "$mcp_dir/notify/configure.py" > /dev/null 2>&1; then
            log_success "Configured MCP: notify"
        else
            log_warning "Failed to configure MCP notify"
        fi
    fi
    
    # Install Python dependencies for MCP notify
    if [ -f "$mcp_dir/notify/pyproject.toml" ]; then
        if command -v pip3 &> /dev/null; then
            log_info "Checking MCP dependencies..."
            if pip3 show mcp > /dev/null 2>&1; then
                log_info "MCP package already installed"
            else
                log_warning "MCP package not found. Install with:"
                echo "  pip3 install mcp"
            fi
        fi
    fi
}

show_status() {
    echo ""
    echo "============================================"
    echo "            Installation Summary            "
    echo "============================================"
    echo ""
    
    if [ -f "$OPENCODE_CONFIG_DIR/AGENTS.md" ]; then
        log_info "Global rules: $OPENCODE_CONFIG_DIR/AGENTS.md"
        echo ""
    fi
    
    log_info "Agents installed in: $OPENCODE_CONFIG_DIR/agent/"
    ls -1 "$OPENCODE_CONFIG_DIR/agent/"*.md 2>/dev/null | while read f; do
        echo "  - $(basename "$f")"
    done
    
    echo ""
    log_info "Skills installed in: $OPENCODE_CONFIG_DIR/skill/"
    for dir in "$OPENCODE_CONFIG_DIR/skill"/*/; do
        if [ -d "$dir" ]; then
            echo "  - $(basename "$dir")"
        fi
    done
    
    echo ""
    if [ -f "$OPENCODE_CONFIG_DIR/opencode.json" ]; then
        if grep -q '"mcp"' "$OPENCODE_CONFIG_DIR/opencode.json" 2>/dev/null; then
            log_info "MCP servers configured in: $OPENCODE_CONFIG_DIR/opencode.json"
            grep -o '"[a-z]*":' "$OPENCODE_CONFIG_DIR/opencode.json" 2>/dev/null | grep -v '"mcp"' | head -5 | while read server; do
                echo "  - ${server//[\":]/}"
            done
        fi
    fi
    
    echo ""
    if [ -d "$BACKUP_DIR" ]; then
        local backup_size=$(du -sh "$BACKUP_DIR" 2>/dev/null | cut -f1)
        log_info "Backups stored in: $BACKUP_DIR ($backup_size / ${BACKUP_MAX_SIZE_MB}MB limit)"
        ls -1 "$BACKUP_DIR" 2>/dev/null | tail -5 | while read b; do
            echo "  - $b"
        done
    fi
    
    echo ""
    echo "============================================"
}

show_help() {
    echo "OpenCode Configuration Installer"
    echo ""
    echo "Usage: $0 [command]"
    echo ""
    echo "Commands:"
    echo "  install     Install agents, skills, and MCP servers (default)"
    echo "  agents      Install only agents"
    echo "  skills      Install only skills"
    echo "  mcp         Configure MCP servers only"
    echo "  status      Show current installation status"
    echo "  diff        Show differences with installed versions"
    echo "  backup      Create backup of current config"
    echo "  restore     Restore from backup"
    echo "  help        Show this help"
    echo ""
    echo "Backup rotation: ${BACKUP_MAX_SIZE_MB}MB max (oldest removed first)"
    echo ""
}

cmd_diff() {
    echo "Comparing with installed versions..."
    echo ""
    
    local has_diff=false
    
    # Compare agents
    for agent_file in "$SCRIPT_DIR/agents"/*.md; do
        if [ -f "$agent_file" ]; then
            local name=$(basename "$agent_file")
            local dest="$OPENCODE_CONFIG_DIR/agent/$name"
            if show_diff "$agent_file" "$dest" "$name"; then
                has_diff=true
            fi
        fi
    done
    
    # Compare skills
    for skill_subdir in "$SCRIPT_DIR/skills"/*; do
        if [ -d "$skill_subdir" ]; then
            local skill_name=$(basename "$skill_subdir")
            if [ -f "$skill_subdir/SKILL.md" ]; then
                local dest="$OPENCODE_CONFIG_DIR/skill/$skill_name/SKILL.md"
                if show_diff "$skill_subdir/SKILL.md" "$dest" "skill/$skill_name"; then
                    has_diff=true
                fi
            fi
        fi
    done
    
    if [ "$has_diff" = false ]; then
        log_success "All files are up to date!"
    fi
}

cmd_backup() {
    log_info "Creating full backup..."
    mkdir -p "$BACKUP_DIR"
    
    create_backup "$OPENCODE_CONFIG_DIR/agent" "agents" || true
    create_backup "$OPENCODE_CONFIG_DIR/skill" "skills" || true
    
    if [ -f "$OPENCODE_CONFIG_DIR/opencode.json" ]; then
        mkdir -p "$BACKUP_DIR/config-$TIMESTAMP"
        cp "$OPENCODE_CONFIG_DIR/opencode.json" "$BACKUP_DIR/config-$TIMESTAMP/"
        log_success "Config backed up"
    fi
    
    log_success "Backup complete: $BACKUP_DIR/*-$TIMESTAMP"
}

cmd_restore() {
    echo "Available backups:"
    ls -1 "$BACKUP_DIR" 2>/dev/null | sort -r | head -10
    echo ""
    read -p "Enter backup name to restore (or 'cancel'): " backup_name
    
    if [ "$backup_name" = "cancel" ]; then
        log_info "Restore cancelled"
        return
    fi
    
    local backup_path="$BACKUP_DIR/$backup_name"
    if [ ! -d "$backup_path" ]; then
        log_error "Backup not found: $backup_path"
        return 1
    fi
    
    # Determine backup type from name
    if [[ "$backup_name" == agents-* ]]; then
        cp -r "$backup_path"/* "$OPENCODE_CONFIG_DIR/agent/"
        log_success "Agents restored from $backup_name"
    elif [[ "$backup_name" == skills-* ]]; then
        cp -r "$backup_path"/* "$OPENCODE_CONFIG_DIR/skill/"
        log_success "Skills restored from $backup_name"
    elif [[ "$backup_name" == config-* ]]; then
        cp "$backup_path/opencode.json" "$OPENCODE_CONFIG_DIR/"
        log_success "Config restored from $backup_name"
    else
        log_error "Unknown backup type"
    fi
}

# Main
case "${1:-install}" in
    install)
        echo ""
        echo "OpenCode Configuration Installer"
        echo "================================="
        echo ""
        install_rules
        install_agents
        install_skills
        install_mcp
        show_status
        ;;
    agents)
        install_agents
        ;;
    skills)
        install_skills
        ;;
    mcp)
        install_mcp
        ;;
    status)
        show_status
        ;;
    diff)
        cmd_diff
        ;;
    backup)
        cmd_backup
        ;;
    restore)
        cmd_restore
        ;;
    help|--help|-h)
        show_help
        ;;
    *)
        log_error "Unknown command: $1"
        show_help
        exit 1
        ;;
esac
