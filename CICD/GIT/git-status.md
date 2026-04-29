- `origin/develop` is a remote‑tracking branch
  - ✅ Local (stored in your .git directory)
  - ✅ Represents the state of develop on the remote origin
  - ✅ Updated only by git fetch / git pull
  - ❌ You do not commit to it
  - ❌ You do not move it manually

- `develop` is a local working branch
  - ✅ A normal branch you own, and are working on
  - ✅ You can commit, rebase, reset, delete it
  - ❌ Not automatically updated from the server

- `git status` will compare the remote-tracking branch with the local working branch:
  - our branch is up to date with 'origin/develop'
  - our branch is ahead of 'origin/develop' by 2 commits.
  - our branch is behind 'origin/develop' by 3 commits.
  - our branch and 'origin/develop' have diverged, and have 2 and 3 different commits each.
