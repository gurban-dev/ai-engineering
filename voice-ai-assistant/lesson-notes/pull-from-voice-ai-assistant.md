# Synchronising voice-ai-assistant with the Upstream Repository

This guide explains how to retrieve the latest changes from the `voice-ai-assistant` subdirectory in the upstream GitHub repository while preserving your own local work.

**Upstream repository:**  
[https://github.com/gurban-dev/ai-engineering](https://github.com/gurban-dev/ai-engineering)

Before synchronising: Make sure all your local changes are committed and your working tree is clean. Run the following command to check:

```powershell
git status
```

If Git reports nothing to commit, working tree clean, you are ready to proceed.

If Git reports modified, deleted, or untracked files, you have local changes that have not been committed.

To save these changes in your local repository, run:

```powershell
git add -A
git commit -m "commit-message-describing-your-changes"
```

## 1. Initial Synchronisation

### Step 1. Fetch upstream changes

```powershell
# Download the latest commits from the upstream main branch.
git fetch second-remote main
```

### Step 2. Extract the voice-ai-assistant subdirectory

```powershell
# Extract the subdirectory's Git history into a separate branch.
git subtree split --prefix=voice-ai-assistant second-remote/main -b upstream-voice-ai-assistant
```

### Step 3. Merge upstream changes

```powershell
# Merge the extracted project into your local repository.
# Allow unrelated histories because the repositories were created independently.
git merge upstream-voice-ai-assistant --allow-unrelated-histories
```

If Git reports merge conflicts, open the affected files in VS Code, compare both versions and resolve the conflicts manually.

After resolving them:

```powershell
# Stage all resolved changes.
git add -A

# Complete the merge.
git commit -m "Merge upstream voice-ai-assistant updates"
```

---

## 2. Synchronising Future Updates

After completing the initial synchronisation, you no longer need `--allow-unrelated-histories` because the Git histories have been connected.

Whenever new upstream changes are available, run:

### Step 1. Fetch upstream changes

```powershell
# Download the latest upstream commits.
git fetch second-remote main
```

### Step 2. Delete the previous extraction branch

```powershell
# Remove the previous temporary extraction branch.
git branch -D upstream-voice-ai-assistant
```

### Step 3. Extract the updated subdirectory

```powershell
# Create a new branch containing the latest upstream subdirectory.
git subtree split --prefix=voice-ai-assistant second-remote/main -b upstream-voice-ai-assistant
```

### Step 4. Merge the updates

```powershell
# Merge the latest upstream changes into your local project.
git merge upstream-voice-ai-assistant
```

If conflicts occur, resolve them in VS Code, then run:

```powershell
# Stage all resolved changes.
git add -A

# Complete the merge.
git commit -m "Update voice-ai-assistant from upstream"
```