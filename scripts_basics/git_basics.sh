#!/bin/bash
# Common Git Commands Reference

# --- SETUP ---
git config --global user.name "Your Name"
git config --global user.email "you@example.com"

# --- INIT & CLONE ---
git init                          # Initialize a new local repo
git clone <url>                   # Clone a remote repo locally

# --- STATUS & LOG ---
git status                        # Show working tree status
git log --oneline --graph         # Compact commit history with branch graph
git diff                          # Show unstaged changes
git diff --staged                 # Show staged changes

# --- STAGING & COMMITTING ---
git add <file>                    # Stage a specific file
git add .                         # Stage all changes
git commit -m "message"           # Commit staged changes
git commit --amend                # Amend the last commit

# --- BRANCHING ---
git branch                        # List local branches
git branch <name>                 # Create a new branch
git switch <name>                 # Switch to a branch
git switch -c <name>              # Create and switch to a new branch
git branch -d <name>              # Delete a branch (safe)
git branch -D <name>              # Force delete a branch

# --- MERGING & REBASING ---
git merge <branch>                # Merge branch into current branch
git rebase <branch>               # Rebase current branch onto another

# --- REMOTE ---
git remote -v                     # List remotes
git remote add origin <url>       # Add a remote
git fetch                         # Fetch changes without merging
git pull                          # Fetch and merge from remote
git push origin <branch>          # Push branch to remote
git push -u origin <branch>       # Push and set upstream tracking

# --- UNDOING ---
git restore <file>                # Discard unstaged changes in a file
git restore --staged <file>       # Unstage a file
git revert <commit>               # Create a new commit that undoes a commit
git reset --hard HEAD~1           # Discard last commit and all its changes (destructive)

# --- STASHING ---
git stash                         # Stash current changes
git stash pop                     # Apply and remove latest stash
git stash list                    # List all stashes

# --- TAGGING ---
git tag                           # List tags
git tag -a v1.0 -m "message"     # Create an annotated tag
git push origin --tags            # Push all tags to remote
