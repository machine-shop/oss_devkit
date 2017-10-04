import subprocess

# content of test_sample.py
def test_attemp():
    process = subprocess.Popen(["git", "hub", "sync"])
    process = subprocess.Popen(["cd", "OutsideHacks/.git/git-hub"])
    process = subprocess.Popen(["git", "hub", "search", "-c", "test"], stdout=subprocess.PIPE)
    assert "help" == str(process.stdout.read())
