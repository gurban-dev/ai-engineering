# Cloning the `voice-ai-assistant` Subdirectory

This guide explains how to retrieve only the `voice-ai-assistant` subdirectory from the upstream GitHub repository using Git sparse checkout.

**Upstream repository:** https://github.com/gurban-dev/ai-engineering

## 1. Initial Clone

### 1. Initialise the Git repository

```powershell
git init
```

Creates a new, empty Git repository in the current directory.

### 2. Add the upstream repository as a remote

```powershell
git remote add origin https://github.com/gurban-dev/ai-engineering.git
```

Connects your local repository to the upstream GitHub repository and names the remote `origin`.

### 3. Enable sparse checkout

```powershell
git config core.sparseCheckout true
```

Enables sparse checkout, allowing Git to check out only specified parts of the repository.

### 4. Specify the subdirectory to check out

```powershell
git sparse-checkout set voice-ai-assistant
```

Tells Git to check out only the contents of the `voice-ai-assistant` subdirectory.

### 5. Fetch the upstream repository

```powershell
git fetch --depth=1 origin main
```

Downloads the latest commit from the upstream `main` branch without downloading the complete commit history.

### 6. Check out the main branch

```powershell
git checkout main
```

Creates and switches to your local `main` branch, checking out the files specified by sparse checkout.

---

# Synchronising `voice-ai-assistant` with the Upstream Repository

After completing the initial clone, run the following commands whenever you want to retrieve the latest changes from GitHub.

### 1. Fetch upstream changes

```powershell
git fetch origin main
```

Downloads the latest commits from the upstream `main` branch without automatically modifying your local files.

### 2. Overwrite local files with upstream changes

```powershell
git reset --hard origin/main
```

Resets your local `main` branch to match the latest upstream `main` branch, replacing locally tracked files with their upstream versions.

No local changes need to be preserved because the cloned directory is not used for independent development.