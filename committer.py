import subprocess
import random
from datetime import datetime, timedelta
import os


def run_git_command(command):
    """ Run a git command and return its output """
    try:
        result = subprocess.check_output(command, stderr=subprocess.STDOUT,
                                         shell=True, text=True)
        return result.strip().split('\n')
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.output}")
        return []


def get_uncommitted_files():
    """ Get list of files that are uncommitted """
    # Files that are modified or untracked
    modified = run_git_command("git ls-files --modified")
    untracked = run_git_command("git ls-files --others --exclude-standard")
    return modified + untracked


def filter_ignored_files(files):
    """ Filter out files that are ignored by .gitignore """
    unignored_files = []
    for file in files:
        # Check if file is ignored using git check-ignore
        is_ignored = run_git_command(f"git check-ignore {file}")
        if not is_ignored:
            unignored_files.append(file)
    return unignored_files


def commit_files(start_date):
    """Commit files with a unique message on sequential dates with random times."""
    uncommitted_files = get_uncommitted_files()
    # Filter out the ignored files
    relevant_files = filter_ignored_files(uncommitted_files)

    date = datetime.strptime(start_date, "%Y-%m-%d")
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    date.replace(hour=hour, minute=minute,
                 second=second)

    for file in relevant_files:
        timestamp = date.isoformat()
        # print(file)
        # print(timestamp)
        run_git_command(f"git add '{file}'")
        run_git_command(
            f"GIT_COMMITTER_DATE='{timestamp}' git commit -m 'feat: adding file {file}' --date='{timestamp}'")

        date += timedelta(hours=random.randint(12, 48),
                          minutes=random.randint(0, 59),
                          seconds=random.randint(0, 59))


if __name__ == "__main__":
    import sys

    start_date = sys.argv[1]  # Expecting date in YYYY-MM-DD format
    commit_files(start_date)