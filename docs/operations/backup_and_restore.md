# Backup and Restore Guide

This project automatically backs up the `master` branch every night.

## Backup Workflow
- A scheduled GitHub Action creates a branch named `backup/YYYYMMDD`.
- The workflow archives the repository as `repo-YYYY-MM-DD.zip` and uploads it to GitHub Releases.

## Restore Procedure
1. Ensure your working tree is clean.
2. Run `scripts/restore_latest.sh`.
3. The script fast-forwards `master` to the newest backup and runs validation scripts.

## Troubleshooting
- If no backup branch is found, check that the backup workflow succeeded.
- Validation failures indicate repository inconsistencies; run scripts manually for details.
- Network errors may require retrying once connectivity is restored.
