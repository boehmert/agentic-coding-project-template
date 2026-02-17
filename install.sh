#!/bin/bash
# Spec-Driven Development Framework Installer (Unix/Mac/Linux)
# Usage: curl -fsSL https://raw.githubusercontent.com/Carsten-Boehmert_wkl/copilot-spec-framework/main/install.sh | bash

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

print_success() { echo -e "${GREEN}$1${NC}"; }
print_info() { echo -e "${CYAN}$1${NC}"; }
print_error() { echo -e "${RED}$1${NC}"; }
print_warning() { echo -e "${YELLOW}$1${NC}"; }

# Parse arguments
TARGET_PATH="."
SHOW_HELP=false

while [[ $# -gt 0 ]]; do
    case $1 in
        -p|--path)
            TARGET_PATH="$2"
            shift 2
            ;;
        -h|--help)
            SHOW_HELP=true
            shift
            ;;
        *)
            print_error "Unknown option: $1"
            exit 1
            ;;
    esac
done

if [ "$SHOW_HELP" = true ]; then
    cat << EOF
Spec-Driven Development Framework Installer

Usage:
  curl -fsSL https://raw.githubusercontent.com/.../install.sh | bash
  
Or with parameters:
  ./install.sh -p ./my-project

Options:
  -p, --path    Target directory (default: current directory)
  -h, --help    Show this help message

What it does:
  1. Downloads the framework from GitHub
  2. Copies .github/ folder to your project
  3. Provides next steps

EOF
    exit 0
fi

print_info "🚀 Installing Spec-Driven Development Framework..."

# Check if git is installed
if ! command -v git &> /dev/null; then
    print_error "❌ Git is not installed. Please install Git first."
    exit 1
fi

# Create target directory if needed
if [ ! -d "$TARGET_PATH" ]; then
    mkdir -p "$TARGET_PATH"
fi

TARGET_PATH=$(cd "$TARGET_PATH" && pwd)
print_info "📂 Target directory: $TARGET_PATH"

# Check if .github already exists
if [ -d "$TARGET_PATH/.github" ]; then
    print_warning "⚠️  .github folder already exists."
    read -p "Create backup? (y/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        BACKUP_PATH="${TARGET_PATH}/.github_backup_$(date +%Y%m%d_%H%M%S)"
        mv "$TARGET_PATH/.github" "$BACKUP_PATH"
        print_success "✅ Backed up to: $BACKUP_PATH"
    else
        print_error "❌ Installation cancelled. Please remove or backup .github folder manually."
        exit 1
    fi
fi

# Clone framework to temp directory
TEMP_DIR=$(mktemp -d)
print_info "📥 Downloading framework..."

trap "rm -rf $TEMP_DIR" EXIT

git clone --quiet --depth 1 https://github.com/Carsten-Boehmert_wkl/copilot-spec-framework.git "$TEMP_DIR"

# Copy .github folder
print_info "📋 Copying framework files..."
cp -r "$TEMP_DIR/.github" "$TARGET_PATH/"

# Copy context file if exists
if [ -f "$TEMP_DIR/Spec-Driven-Framework-Context.md" ]; then
    cp "$TEMP_DIR/Spec-Driven-Framework-Context.md" "$TARGET_PATH/"
fi

print_success "✅ Framework installed successfully!"

cat << EOF

📚 Next steps:

1. Open this project in VS Code
2. Run the repo-bootstrap prompt:
   
   @workspace /prompt repo-bootstrap
   
   Project: Your Project Name
   Description: What your project does
   Tech Stack: Your technologies

3. Create your first Workorder:
   
   @workspace /prompt create-workorder

📖 Documentation:
   https://confluence.wolterskluwer.io/spaces/~Carsten.Boehmert/pages/1012292066/Spec-Driven+Development+Framework

EOF
