import pytest
import tempfile
import shutil
import os
import subprocess
import re
import yaml

@pytest.fixture(scope="module")
def gh_repo_dir():
    gh_repo = 'https://github.com/SeraYang1/OutsideHacks'
    repo_name = gh_repo.split('/')[-1]
    tmp_dir = '._test_data'
    repo_dir = os.path.abspath(os.path.join(tmp_dir, repo_name))

    if not os.path.isdir(tmp_dir):
        os.makedirs(tmp_dir)

    print(f'Cloning test repository {gh_repo}')
    if not os.path.isdir(repo_dir):
        subprocess.run(['git', 'clone', '--depth=1', gh_repo], cwd=tmp_dir)

    os.chdir(repo_dir)
    if not os.path.isfile('.git/git-hub/pull-requests.toml'):
        print('Syncing with GitHub...')
        process = subprocess.Popen(["git", "hub", "sync"])
        process.communicate()
    else:
        print('Using cached GitHub data')

    return os.path.abspath(repo_dir)


@pytest.fixture
def gh_repo(gh_repo_dir):
    os.chdir(gh_repo_dir)
    process = subprocess.Popen(["ls"], stdout=subprocess.PIPE)
    print(str(process.stdout.read()))
    return gh_repo_dir


def test_sync(gh_repo):
    process = subprocess.Popen(["git", "hub", "sync"])
    process.communicate()
    os.chdir('.git/git-hub')
    process = subprocess.Popen(["ls"], stdout=subprocess.PIPE)
    assert "pull-requests.toml" in str(process.stdout.read())
    process = subprocess.Popen(["rm", "pull-requests.toml"])
    process = subprocess.Popen(["ls"], stdout=subprocess.PIPE)
    assert "pull-requests.toml" not in str(process.stdout.read())
    os.chdir('./../../Server')
    process = subprocess.Popen(["git", "hub", "sync"])
    process.communicate()
    os.chdir('./../.git/git-hub')
    process = subprocess.Popen(["ls"], stdout=subprocess.PIPE)
    assert "pull-requests.toml" in str(process.stdout.read())


def test_get_info_working(gh_repo):
    process = subprocess.Popen(["git", "hub", "info", "3"], stdout=subprocess.PIPE)
    assert 'Sera Yang/test adding spaces\\n-Labels: invalid  -Reviewers: None  -Assignees: None  -Milestones: None' in str(process.stdout.read())


def test_get_info_out_of_bounds(gh_repo):
    process = subprocess.Popen(["git", "hub", "info", "10"], stdout=subprocess.PIPE)
    assert "Could not find PR #10. Run 'git hub sync' and try again." in str(process.stdout.read())


def test_search_keyword(gh_repo):
    process = subprocess.Popen(["git", "hub", "search", "space"], stdout=subprocess.PIPE)
    if(re.search(r".*Sera Yang/test adding spaces : 2017-09-18.*\\n.*Sera Yang/space space : 2017-08-28.*", str(process.stdout.read()))):
        assert True
    else:
        assert False


def test_search_keyword_sorted(gh_repo):
    process = subprocess.Popen(["git", "hub", "search", "space", "-s", "increasing"], stdout=subprocess.PIPE)
    if(re.search(r".*Sera Yang/space space : 2017-08-28.*\\n.*Sera Yang/test adding spaces : 2017-09-18.*", str(process.stdout.read()))):
        assert True
    else:
        assert False


def test_search_open(gh_repo):
    process = subprocess.Popen(["git", "hub", "search", "-o", "open"], stdout=subprocess.PIPE)
    results = str(process.stdout.read())
    if(len(re.findall(r"Sera Yang/", results)) == 1):
        assert True
    else:
        assert False


def test_search_none(gh_repo):
    process = subprocess.Popen(["git", "hub", "search", "haha"], stdout=subprocess.PIPE)
    assert "Could not find in pull requests. Update your pull requests with 'git hub sync' and try again." in str(process.stdout.read())


def test_search_branch(gh_repo):
    process = subprocess.Popen(["git", "hub", "search", "-b", "test"], stdout=subprocess.PIPE)
    if(re.search(r".*Sera Yang/test adding spaces : 2017-09-18.*\\n.* Sera Yang/testing testing pull : 2017-08-28.*", str(process.stdout.read()))):
        assert True
    else:
        assert False


def test_search_all(gh_repo):
    process = subprocess.Popen(["git", "hub", "search"], stdout=subprocess.PIPE)
    if(re.search(r"(.*Sera Yang/.*\\n){4}.*Sera Yang/.*", str(process.stdout.read()))):
        assert True
    else:
        assert False
