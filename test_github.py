import subprocess

# content of test_sample.py
def test_attemp():
    process = subprocess.Popen(["git", "hub", "sync"])
    process = subprocess.Popen(["ls"], stdout=subporcess.PIPE)
    assert "WHAT" == str(process.stdout.read())
