import praw
from praw.models import MoreComments


def display_all_comments(comments, level):
    print((" " * level) + (">" * level) + comments.body)
    for commentReply in comments.replies:
        display_all_comments(commentReply, level + 1)
        print()


reddit = praw.Reddit(client_id="7vOWHznFDrqBVA", client_secret="ExRrk05OkZat5VAYNIARhoQVS0o",
                     user_agent="windows:UniHonoursApp:v1.0.0 (by /u/Delacarpet)")

submissionLink = input("Enter Reddit URL to perform ABSA\n")
submission = reddit.submission(url=submissionLink)

submission.comments.replace_more(limit=None)

for comment in submission.comments:
    display_all_comments(comment, 0)


