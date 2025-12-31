#!/bin/bash
# OpenCode Configuration Installer
# Installs agents and skills with automatic backup and i18n support

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

# i18n Configuration
DEFAULT_LANG="fr"
FALLBACK_LANG="fr"  # Fallback to default language if requested lang not found
LANG="$DEFAULT_LANG"

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

# Get file path with fallback support
# Returns: path to file (with fallback if needed) and sets USED_FALLBACK=true if fallback was used
get_i18n_path() {
    local base_dir="$1"
    local file_path="$2"
    local lang="$3"
    
    USED_FALLBACK=false
    
    local primary_path="$base_dir/$lang/$file_path"
    local fallback_path="$base_dir/$FALLBACK_LANG/$file_path"
    
    if [ -e "$primary_path" ]; then
        echo "$primary_path"
    elif [ -e "$fallback_path" ]; then
        USED_FALLBACK=true
        echo "$fallback_path"
    else
        echo ""
    fi
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
    log_info "Installing agents (lang: $LANG)..."
    
    local agent_dir="$OPENCODE_CONFIG_DIR/agent"
    local source_dir="$SCRIPT_DIR/agents/$LANG"
    local fallback_dir="$SCRIPT_DIR/agents/$FALLBACK_LANG"
    
    mkdir -p "$agent_dir"
    
    # Backup existing agents (ignore if empty)
    create_backup "$agent_dir" "agents" || true
    
    # Check if language directory exists
    if [ ! -d "$source_dir" ]; then
        if [ -d "$fallback_dir" ]; then
            log_warning "Language '$LANG' not found for agents, using fallback '$FALLBACK_LANG'"
            source_dir="$fallback_dir"
        else
            log_error "No agents found for language '$LANG' or fallback '$FALLBACK_LANG'"
            return 1
        fi
    fi
    
    # Install each agent
    for agent_file in "$source_dir"/*.md; do
        if [ -f "$agent_file" ]; then
            local agent_name=$(basename "$agent_file")
            local dest="$agent_dir/$agent_name"
            local fallback_used=""
            
            # Check if we need fallback for this specific file
            if [ ! -f "$SCRIPT_DIR/agents/$LANG/$agent_name" ] && [ -f "$SCRIPT_DIR/agents/$FALLBACK_LANG/$agent_name" ]; then
                agent_file="$SCRIPT_DIR/agents/$FALLBACK_LANG/$agent_name"
                fallback_used=" (fallback: $FALLBACK_LANG)"
            fi
            
            if [ -f "$dest" ]; then
                if diff -q "$agent_file" "$dest" > /dev/null 2>&1; then
                    log_info "Agent $agent_name unchanged, skipping"
                    continue
                else
                    log_warning "Agent $agent_name will be updated$fallback_used"
                fi
            fi
            
            cp "$agent_file" "$dest"
            log_success "Installed: $agent_name$fallback_used"
        fi
    done
}

install_skills() {
    log_info "Installing skills (lang: $LANG)..."
    
    local skill_dir="$OPENCODE_CONFIG_DIR/skill"
    local source_dir="$SCRIPT_DIR/skills/$LANG"
    local fallback_dir="$SCRIPT_DIR/skills/$FALLBACK_LANG"
    
    mkdir -p "$skill_dir"
    
    # Backup existing skills (ignore if empty)
    create_backup "$skill_dir" "skills" || true
    
    # Check if language directory exists
    if [ ! -d "$source_dir" ]; then
        if [ -d "$fallback_dir" ]; then
            log_warning "Language '$LANG' not found for skills, using fallback '$FALLBACK_LANG'"
            source_dir="$fallback_dir"
        else
            log_error "No skills found for language '$LANG' or fallback '$FALLBACK_LANG'"
            return 1
        fi
    fi
    
    # Install each skill (they're in subdirectories)
    for skill_subdir in "$source_dir"/*; do
        if [ -d "$skill_subdir" ]; then
            local skill_name=$(basename "$skill_subdir")
            local dest_dir="$skill_dir/$skill_name"
            local fallback_used=""
            mkdir -p "$dest_dir"
            
            local skill_file="$skill_subdir/SKILL.md"
            
            # Check if we need fallback for this specific skill
            if [ ! -f "$skill_file" ] && [ -f "$SCRIPT_DIR/skills/$FALLBACK_LANG/$skill_name/SKILL.md" ]; then
                skill_file="$SCRIPT_DIR/skills/$FALLBACK_LANG/$skill_name/SKILL.md"
                fallback_used=" (fallback: $FALLBACK_LANG)"
            fi
            
            if [ -f "$skill_file" ]; then
                local dest="$dest_dir/SKILL.md"
                
                if [ -f "$dest" ]; then
                    if diff -q "$skill_file" "$dest" > /dev/null 2>&1; then
                        log_info "Skill $skill_name unchanged, skipping"
                        continue
                    else
                        log_warning "Skill $skill_name will be updated$fallback_used"
                    fi
                fi
                
                cp "$skill_file" "$dest"
                log_success "Installed skill: $skill_name$fallback_used"
            fi
        fi
    done
}

install_rules() {
    log_info "Installing rules (lang: $LANG)..."
    
    local source_file="$SCRIPT_DIR/AGENTS.$LANG.md"
    local fallback_file="$SCRIPT_DIR/AGENTS.$FALLBACK_LANG.md"
    local dest_file="$OPENCODE_CONFIG_DIR/AGENTS.md"
    local fallback_used=""
    
    # Check for language-specific file, then fallback
    if [ ! -f "$source_file" ]; then
        if [ -f "$fallback_file" ]; then
            log_warning "AGENTS.$LANG.md not found, using fallback AGENTS.$FALLBACK_LANG.md"
            source_file="$fallback_file"
            fallback_used=" (fallback: $FALLBACK_LANG)"
        else
            log_warning "No AGENTS.md found for any language, skipping"
            return 0
        fi
    fi
    
    if [ -f "$dest_file" ]; then
        if diff -q "$source_file" "$dest_file" > /dev/null 2>&1; then
            log_info "AGENTS.md unchanged, skipping"
            return 0
        else
            log_warning "AGENTS.md will be updated$fallback_used"
        fi
    fi
    
    cp "$source_file" "$dest_file"
    log_success "Installed AGENTS.md (global rules)$fallback_used"
}

install_mcp() {
    log_info "Configuring MCP servers..."
    
    local servers_dir="$SCRIPT_DIR/servers"
    
    if [ ! -d "$servers_dir" ]; then
        log_warning "No servers directory found, skipping"
        return 0
    fi
    
    # Setup notify server venv and dependencies
    if [ -d "$servers_dir/notify" ]; then
        local notify_dir="$servers_dir/notify"
        local venv_dir="$notify_dir/.venv"
        
        # Create venv if it doesn't exist
        if [ ! -d "$venv_dir" ]; then
            log_info "Creating virtual environment for MCP notify..."
            python3 -m venv "$venv_dir"
            log_success "Virtual environment created"
        fi
        
        # Install dependencies if not already installed
        local needs_install=false
        if ! "$venv_dir/bin/python" -c "import mcp" 2>/dev/null; then
            needs_install=true
        fi
        if ! "$venv_dir/bin/python" -c "import objc" 2>/dev/null; then
            needs_install=true
        fi
        
        if [ "$needs_install" = true ]; then
            log_info "Installing MCP dependencies (mcp, pyobjc)..."
            "$venv_dir/bin/pip" install --quiet mcp pyobjc
            log_success "Dependencies installed"
        else
            log_info "Dependencies already installed"
        fi
        
        # Configure notify server
        if [ -f "$notify_dir/configure.py" ]; then
            if python3 "$notify_dir/configure.py" > /dev/null 2>&1; then
                log_success "Configured MCP: notify"
            else
                log_warning "Failed to configure MCP notify"
            fi
        fi
    fi
    
    # Setup screenshot server venv and dependencies
    if [ -d "$servers_dir/screenshot" ]; then
        local screenshot_dir="$servers_dir/screenshot"
        local venv_dir="$screenshot_dir/.venv"
        
        # Create venv if it doesn't exist
        if [ ! -d "$venv_dir" ]; then
            log_info "Creating virtual environment for MCP screenshot..."
            python3 -m venv "$venv_dir"
            log_success "Virtual environment created"
        fi
        
        # Install dependencies if not already installed
        local needs_install=false
        if ! "$venv_dir/bin/python" -c "import mcp" 2>/dev/null; then
            needs_install=true
        fi
        if ! "$venv_dir/bin/python" -c "import Quartz" 2>/dev/null; then
            needs_install=true
        fi
        
        if [ "$needs_install" = true ]; then
            log_info "Installing MCP dependencies (mcp, pyobjc-framework-Quartz)..."
            "$venv_dir/bin/pip" install --quiet mcp pyobjc-framework-Quartz
            log_success "Dependencies installed"
        else
            log_info "Dependencies already installed"
        fi
        
        # Configure screenshot server
        if [ -f "$screenshot_dir/configure.py" ]; then
            if python3 "$screenshot_dir/configure.py" > /dev/null 2>&1; then
                log_success "Configured MCP: screenshot"
            else
                log_warning "Failed to configure MCP screenshot"
            fi
        fi
    fi
    
    # Setup lsmcp server (LSP tools for Claude)
    if [ -d "$servers_dir/lsmcp" ]; then
        local lsmcp_dir="$servers_dir/lsmcp"
        
        # Check Node.js version (lsmcp requires >= 22)
        if command -v node &> /dev/null; then
            local node_version=$(node --version | sed 's/v//' | cut -d. -f1)
            if [ "$node_version" -ge 22 ] 2>/dev/null; then
                # Node.js >= 22 available, configure lsmcp
                if [ -f "$lsmcp_dir/configure.py" ]; then
                    if python3 "$lsmcp_dir/configure.py" > /dev/null 2>&1; then
                        log_success "Configured MCP: lsmcp (LSP tools)"
                    else
                        log_warning "Failed to configure MCP lsmcp"
                    fi
                fi
            else
                log_warning "lsmcp requires Node.js >= 22 (found v$node_version), skipping"
            fi
        else
            log_warning "lsmcp requires Node.js >= 22 (not found), skipping"
        fi
    fi
    
    # Setup sequential-thinking server (structured reasoning via npx)
    if [ -d "$servers_dir/sequential-thinking" ]; then
        local st_dir="$servers_dir/sequential-thinking"
        
        # Check Node.js version (sequential-thinking requires >= 18)
        if command -v node &> /dev/null; then
            local node_version=$(node --version | sed 's/v//' | cut -d. -f1)
            if [ "$node_version" -ge 18 ] 2>/dev/null; then
                # Node.js >= 18 available, configure sequential-thinking
                if [ -f "$st_dir/configure.py" ]; then
                    if python3 "$st_dir/configure.py" > /dev/null 2>&1; then
                        log_success "Configured MCP: sequential-thinking"
                    else
                        log_warning "Failed to configure MCP sequential-thinking"
                    fi
                fi
            else
                log_warning "sequential-thinking requires Node.js >= 18 (found v$node_version), skipping"
            fi
        else
            log_warning "sequential-thinking requires Node.js >= 18 (not found), skipping"
        fi
    fi
}

show_status() {
    echo ""
    echo "============================================"
    echo "            Installation Summary            "
    echo "============================================"
    echo ""
    
    # Show language
    if [ "$LANG" = "$DEFAULT_LANG" ]; then
        log_info "Language: $LANG (default)"
    else
        log_info "Language: $LANG"
    fi
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
        if command -v jq &> /dev/null && grep -q '"mcp"' "$OPENCODE_CONFIG_DIR/opencode.json" 2>/dev/null; then
            log_info "MCP servers configured in: $OPENCODE_CONFIG_DIR/opencode.json"
            jq -r '.mcp // {} | keys[]' "$OPENCODE_CONFIG_DIR/opencode.json" 2>/dev/null | while read server; do
                local enabled=$(jq -r ".mcp.\"$server\".enabled // false" "$OPENCODE_CONFIG_DIR/opencode.json")
                if [ "$enabled" = "true" ]; then
                    echo "  - $server (enabled)"
                else
                    echo "  - $server (disabled)"
                fi
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
    echo "Usage: $0 [command] [options]"
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
    echo "Options:"
    echo "  -l, --lang LANG    Set installation language (default: $DEFAULT_LANG)"
    echo "                     Available: fr, en"
    echo "                     Fallback: $FALLBACK_LANG (if requested lang not found)"
    echo ""
    echo "Examples:"
    echo "  $0 install              # Install in default language ($DEFAULT_LANG)"
    echo "  $0 install --lang=en    # Install in English"
    echo "  $0 install -l fr        # Install in French"
    echo ""
    echo "Backup rotation: ${BACKUP_MAX_SIZE_MB}MB max (oldest removed first)"
    echo ""
}

cmd_diff() {
    echo "Comparing with installed versions (lang: $LANG)..."
    echo ""
    
    local has_diff=false
    local source_agents="$SCRIPT_DIR/agents/$LANG"
    local source_skills="$SCRIPT_DIR/skills/$LANG"
    
    # Fallback if language not found
    [ ! -d "$source_agents" ] && source_agents="$SCRIPT_DIR/agents/$FALLBACK_LANG"
    [ ! -d "$source_skills" ] && source_skills="$SCRIPT_DIR/skills/$FALLBACK_LANG"
    
    # Compare agents
    for agent_file in "$source_agents"/*.md; do
        if [ -f "$agent_file" ]; then
            local name=$(basename "$agent_file")
            local dest="$OPENCODE_CONFIG_DIR/agent/$name"
            if show_diff "$agent_file" "$dest" "$name"; then
                has_diff=true
            fi
        fi
    done
    
    # Compare skills
    for skill_subdir in "$source_skills"/*; do
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

# Parse command line arguments
parse_args() {
    COMMAND="install"
    
    while [[ $# -gt 0 ]]; do
        case $1 in
            -l|--lang)
                LANG="$2"
                shift 2
                ;;
            --lang=*)
                LANG="${1#*=}"
                shift
                ;;
            install|agents|skills|mcp|status|diff|backup|restore|help|--help|-h)
                COMMAND="$1"
                shift
                ;;
            *)
                log_error "Unknown option: $1"
                show_help
                exit 1
                ;;
        esac
    done
}

# Main
parse_args "$@"

case "$COMMAND" in
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
        log_error "Unknown command: $COMMAND"
        show_help
        exit 1
        ;;
esac
