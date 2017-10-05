# import subprocess
# import os
#
# # content of test_sample.py
# def test_search_keyword():
#     os.makedirs("test3")
#     os.chdir(os.getcwd() + "/test3")
#     p = subprocess.Popen(["git", "clone", "https://github.com/SeraYang1/OutsideHacks.git"])
#     p.communicate()
#     os.chdir(os.getcwd() + "/OutsideHacks/.git/git-hub")
#     process = subprocess.Popen(["git", "hub", "sync"])
#     process = subprocess.Popen(["ls"], stdout=subprocess.PIPE)
#     assert "OutsideHacks" in str(process.stdout.read())
#     process = subprocess.Popen(["git", "hub", "sync"])
#     process = subprocess.Popen(["ls"],stdout=subprocess.PIPE)
#     assert "pull-requests.toml" in str(process.stdout.read())
#     process = subprocess.Popen(["git", "hub", "search", "empty"], stdout=subprocess.PIPE)
#     assert str(process.stdout.read()) == '5 \x1b[0;32;40m 0 \x1b[0m Sera Yang/another-pull empty : 2017-09-18'
#
# def test_get_info():
#     process = subprocess.Popen(["git", "hub", "info", "3"])
#     assert str(process.stdout.read()) == '3 \x1b[0;32;40m C \x1b[0m Sera Yang/test adding spaces \n -Labels: invalid  -Reviewers: None  -Assignees: None  -Milestones: None'




import pytest
import tempfile
import shutil
import os
import subprocess


@pytest.fixture(scope="module")
def gh_repo_dir():
    gh_repo = 'https://github.com/SeraYang1/OutsideHacks'
    repo_name = gh_repo.split('/')[-1]

    tmp_dir = tempfile.mkdtemp()
    print(f'Cloning test repository {gh_repo}')
    subprocess.run(['git', 'clone', '--depth=1', gh_repo], cwd=tmp_dir)

    yield os.path.join(os.path.join(tmp_dir, repo_name))

    shutil.rmtree(tmp_dir)


@pytest.fixture
def gh_repo(gh_repo_dir):
    print(f'Changing into repo {gh_repo_dir}')
    os.chdir(gh_repo_dir)
    return gh_repo_dir


def test_status(gh_repo):
    print("repos: " ,os.listdir(gh_repo))
    assert os.listdir(gh_repo) == "hi"


def test_something_else(gh_repo):
    print("Let's ensure the repo isn't cloned twice")
    print(gh_repo)
    subprocess.run(['git', 'pull'])
