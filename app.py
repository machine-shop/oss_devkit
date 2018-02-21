import jinja2
import webpage
import os
from os.path import join as pjoin


def path_to_pic():
    """Finds path to .git folder
    """
    path_repo = os.path.abspath('.')
    while os.path.abspath(path_repo) != '/' and not os.path.isdir(pjoin(path_repo, '.git')):
        path_repo = pjoin(path_repo, '..')
    path_git = pjoin(path_repo, ".git")
    path_pic = pjoin(path_git, "git-hub")
    path_pic = pjoin(path_pic, "PRs.png")
    if os.path.exists(path_pic):
        return path_pic
    return None


def main():
    week_old, week_old_url = webpage.week_old_comments()
    no_discussion, no_discussion_url = webpage.no_discussion()
    most_active, most_active_url = webpage.most_active_prs()
    oldest_pr, oldest_pr_url = webpage.oldest_prs()
    my_prs, my_prs_url = webpage.prs_with_me()
    unmergeable_prs, unmergeable_prs_url = webpage.unmergeable_prs()
    issues_no_comments, issues_no_comments_url = webpage.issues_no_comments()
    closed_pr_refer_tickets, closed_pr_refer_tickets_url = webpage.closed_pr_refer_ticket()
    popular_tickets, popular_tickets_url = webpage.popular_tickets()

    picture = path_to_pic()
    complete_path = os.path.join(os.path.dirname(__file__), 'templates/template.html')
    style = os.path.join(os.path.dirname(__file__), 'templates/style.css')
    script = os.path.join(os.path.dirname(__file__), 'templates/script.js')
    jquery = os.path.join(os.path.dirname(__file__), 'templates/jquery-1.9.1.js')
    path, filename = os.path.split(complete_path)
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(path or './'))
    template = env.get_template(filename)
    out = template.render({'style': style, 'script': script, 'jquery': jquery, 'picture': picture, 'issues_no_comments': issues_no_comments, 'closed_pr_refer_tickets': closed_pr_refer_tickets, 'popular_tickets': popular_tickets, 'week_old': week_old, 'no_discussion': no_discussion, 'active_prs': most_active, 'oldest_prs': oldest_pr, 'my_prs': my_prs, 'unmergeable_prs': unmergeable_prs,
     'issues_no_comments_url': issues_no_comments_url, 'closed_pr_refer_tickets_url': closed_pr_refer_tickets_url, 'popular_tickets_url': popular_tickets_url, 'week_old_url': week_old_url, 'no_discussion_url': no_discussion_url, 'active_prs_url': most_active_url, 'oldest_prs_url': oldest_pr_url, 'my_prs_url': my_prs_url, 'unmergeable_prs_url': unmergeable_prs_url})
    fname = "./output.html"
    print("Template rendered at output.html")
    with open(fname, 'w') as f:
        f.write(out)
