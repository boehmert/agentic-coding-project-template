#!/usr/bin/env pwsh
# Spec-Driven Development Framework Installer (Windows PowerShell)
# Usage: irm https://raw.githubusercontent.com/Carsten-Boehmert_wkl/copilot-spec-framework/main/install.ps1 | iex

param(
    [string]$Path = ".",
    [switch]$Help
)

$ErrorActionPreference = "Stop"

# Colors
function Write-Success { Write-Host $args -ForegroundColor Green }
function Write-Info { Write-Host $args -ForegroundColor Cyan }
function Write-Error { Write-Host $args -ForegroundColor Red }

if ($Help) {
    Write-Host @"
Spec-Driven Development Framework Installer

Usage:
  irm https://raw.githubusercontent.com/.../install.ps1 | iex
  
Or with parameters:
  & install.ps1 -Path ./my-project

Options:
  -Path    Target directory (default: current directory)
  -Help    Show this help message

What it does:
  1. Downloads the framework from GitHub
  2. Copies .github/ folder to your project
  3. Runs repo-bootstrap prompt

"@
    exit 0
}

Write-Info "🚀 Installing Spec-Driven Development Framework..."

# Check if git is available
if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Error "❌ Git is not installed. Please install Git first."
    exit 1
}

# Create target directory if needed
$TargetPath = Resolve-Path $Path -ErrorAction SilentlyContinue
if (-not $TargetPath) {
    New-Item -Path $Path -ItemType Directory -Force | Out-Null
    $TargetPath = Resolve-Path $Path
}

Write-Info "📂 Target directory: $TargetPath"

# Check if .github already exists
$GithubPath = Join-Path $TargetPath ".github"
if (Test-Path $GithubPath) {
    Write-Host "⚠️  .github folder already exists. Backup? (y/n): " -NoNewline -ForegroundColor Yellow
    $response = Read-Host
    if ($response -eq 'y') {
        $backupPath = "${GithubPath}_backup_$(Get-Date -Format 'yyyyMMdd_HHmmss')"
        Move-Item $GithubPath $backupPath
        Write-Success "✅ Backed up to: $backupPath"
    } else {
        Write-Error "❌ Installation cancelled. Please remove or backup .github folder manually."
        exit 1
    }
}

# Clone framework to temp directory
$TempDir = Join-Path $env:TEMP "spec-framework-$(Get-Random)"
Write-Info "📥 Downloading framework..."

try {
    git clone --quiet --depth 1 https://github.com/Carsten-Boehmert_wkl/copilot-spec-framework.git $TempDir
    
    # Copy .github folder
    Write-Info "📋 Copying framework files..."
    Copy-Item -Path (Join-Path $TempDir ".github") -Destination $TargetPath -Recurse -Force
    
    # Copy context file
    if (Test-Path (Join-Path $TempDir "Spec-Driven-Framework-Context.md")) {
        Copy-Item -Path (Join-Path $TempDir "Spec-Driven-Framework-Context.md") -Destination $TargetPath
    }
    
    Write-Success "✅ Framework installed successfully!"
    
    Write-Info @"

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

"@

} catch {
    Write-Error "❌ Installation failed: $_"
    exit 1
} finally {
    # Cleanup
    if (Test-Path $TempDir) {
        Remove-Item -Path $TempDir -Recurse -Force
    }
}
