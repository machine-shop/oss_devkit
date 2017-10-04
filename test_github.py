import subprocess

# content of test_sample.py
def test_attemp():
    process = subprocess.Popen(["git", "hub", "sync"])
    process = subprocess.Popen(["ls"], stdout=subprocess.PIPE)
    assert "OutsideHacks" in str(process.stdout.read())
    process = subprocess.Popen(["cd", "OutsideHacks/.git/git-hub"])
    process = subprocess.Popen(["git", "hub", "sync"])
    process = subprocess.Popen(["ls"],stdout=subprocess.PIPE)
    assert "pull-requests.toml" in str(process.stdout.read())
    process = subprocess.Popen(["git", "hub", "search", "empty"], stdout=subprocess.PIPE)
    assert str(process.stdout.read()) == '5 \x1b[0;32;40m 0 \x1b[0m Sera Yang/another-pull empty : 2017-09-18'
