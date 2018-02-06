import jinja2
import webpage
import os
from os.path import join as pjoin

def path_to_pic():
    """Finds path to .git folder
    """
    path_repo = os.path.abspath('.')
    # if not in directory with .git, keep going back to find file
    while os.path.abspath(path_repo) != '/' and not os.path.isdir(pjoin(path_repo, '.git')):
        path_repo = pjoin(path_repo, '..')
    path_git = pjoin(path_repo, ".git")
    path_pic = pjoin(path_git, "git-hub")
    path_pic = pjoin(path_pic, "PRs.png")
    return path_pic

def main():
    list_of_prs = webpage.week_old_comments()
    no_diss = webpage.no_discussion()
    popular = webpage.most_active_prs()
    oldest = webpage.oldest_prs()
    mine = webpage.prs_with_me()
    unmergeable = webpage.unmergeable_prs()
    #issues_no_comments = webpage.issues_no_comments()
    #closed_pr_refer_tickets = webpage.closed_pr_refer_tickets()
    #popular_tickets = webpage.popular_tickets()
    picture = path_to_pic()
    # print(picture)
    complete_path = os.path.join(os.path.dirname(__file__), 'templates/template.html')
    path, filename = os.path.split(complete_path)
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(path or './'))
    template = env.get_template(filename)
    out = template.render({'week_old':list_of_prs, 'no_discussion':no_diss, 'active_prs':popular, 'oldest_prs':oldest, 'my_prs':mine, 'unmergeable_prs':unmergeable, 'picture':picture})
    fname = "./output.html"
    with open(fname, 'w') as f:
        f.write(out)
