# Spec-Driven Development Framework – Installation

This document describes how to install the framework into your project.

## Quick Install

### Windows (PowerShell)

```powershell
irm https://raw.githubusercontent.com/Carsten-Boehmert_wkl/copilot-spec-framework/main/install.ps1 | iex
```

### macOS / Linux (bash)

```bash
curl -fsSL https://raw.githubusercontent.com/Carsten-Boehmert_wkl/copilot-spec-framework/main/install.sh | bash
```

---

## Install to Specific Directory

### Windows

```powershell
# Download script
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/.../install.ps1" -OutFile install.ps1

# Run with custom path
.\install.ps1 -Path "C:\projects\my-project"
```

### macOS / Linux

```bash
# Download script
curl -fsSL https://raw.githubusercontent.com/.../install.sh -o install.sh
chmod +x install.sh

# Run with custom path
./install.sh --path ./my-project
```

---

## Manual Installation

1. Clone or download the repository
2. Copy the `.github/` folder to your project
3. Optionally copy `Spec-Driven-Framework-Context.md`

```bash
# Clone
git clone https://github.com/Carsten-Boehmert_wkl/copilot-spec-framework.git temp
cp -r temp/.github ./my-project/
rm -rf temp
```

---

## What Gets Installed

```
your-project/
├── .github/
│   ├── agents/              # 7 specialized agents
│   ├── instructions/        # Coding standards
│   ├── prompts/             # Reusable workflows
│   ├── schemas/             # Specification formats
│   ├── copilot-instructions.md
│   └── FRAMEWORK_MANIFEST.md
└── Spec-Driven-Framework-Context.md  # Optional context file
```

---

## After Installation

### 1. Initialize your project

Open in VS Code and run:

```
@workspace /prompt repo-bootstrap

Project: Your Project Name
Description: What your project does
Tech Stack: Python, FastAPI, PostgreSQL
```

This creates:
- `REPO_STATE.md` – Project status tracking
- `workorders/WO_CATALOG.md` – Workorder registry
- `workorders/WO00_repo-bootstrap.md` – Bootstrap workorder
- `docs/adr/` – Architecture decisions folder

### 2. Create your first Workorder

```
@workspace /prompt create-workorder

Task: Implement user authentication
Context: Users need to log in to access protected resources
```

### 3. Run pre-implementation check

```
@workspace /prompt pre-implementation-check WO01
```

---

## Backup Existing .github Folder

Both installers will prompt you if `.github` already exists.

**Manual backup:**

```bash
# Unix/Mac/Git Bash
mv .github .github_backup_$(date +%Y%m%d_%H%M%S)

# PowerShell
Move-Item .github ".github_backup_$(Get-Date -Format 'yyyyMMdd_HHmmss')"
```

---

## Troubleshooting

### Git not found

Install Git:
- Windows: https://git-scm.com/download/win
- Mac: `brew install git` or Xcode Command Line Tools
- Linux: `sudo apt install git` or equivalent

### Permission denied (Unix/Mac)

Make script executable:

```bash
chmod +x install.sh
./install.sh
```

### Script execution disabled (Windows)

Enable script execution temporarily:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\install.ps1
```

---

## Documentation

Full documentation:  
https://confluence.wolterskluwer.io/spaces/~Carsten.Boehmert/pages/1012292066/Spec-Driven+Development+Framework

GitHub Repository:  
https://github.com/Carsten-Boehmert_wkl/copilot-spec-framework
