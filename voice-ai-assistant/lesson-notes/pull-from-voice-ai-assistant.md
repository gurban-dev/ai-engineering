# Clone the `voice-ai-assistant` Subdirectory

Run these commands in PowerShell.

## 1. Initialize Git in voice-ai-assistant-d

```powershell
git init
```

## 4. Add the upstream repository

```powershell
git remote add origin https://github.com/gurban-dev/ai-engineering.git
```

## 5. Enable sparse checkout

```powershell
git config core.sparseCheckout true
```

## 6. Select the subdirectory

```powershell
git sparse-checkout set voice-ai-assistant
```

Includes the entire directory and all nested files and directories.

## 7. Fetch the upstream repository

```powershell
git fetch --depth=1 origin main
```

Downloads the latest commit without the complete Git history.

## 8. Check out the main branch

```powershell
git checkout -b main --track origin/main
```

## Synchronizing with Upstream (After the Initial Pull)

Whenever you want to retrieve the latest changes from GitHub, run the following commands from the repository root.

### 1. Fetch upstream changes

```powershell
git fetch origin main
```

Downloads the latest commits from the upstream `main` branch without modifying local files.

### 2. Update local files

```powershell
git reset --hard origin/main
```

Updates the local branch and working files to match the latest upstream `main` branch.

**Note:** This discards local changes to tracked files.