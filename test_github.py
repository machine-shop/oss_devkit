import subprocess

# content of test_sample.py
def test_attemp():
    process = subprocess.Popen(["git", "hub", "sync"])
    process = subprocess.Popen(["cd", ".git/git_hub"])
