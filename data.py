# This class was created to be the goto for any functions that involve data manipulation or reading.

import os
import xml.etree.ElementTree as ET
import praw


# read xml from file.
def get_xml_data(file):
    tree = ET.parse(file)
    reviews = tree.findall('review')

    text, labels = [], []

    for review in reviews:
        sentences = review.findall('sentence');
        for sentence in sentences:
            print(sentence.find('text').text)
            aspects = sentence.findall('aspectTerms/aspectTerm')
            for aspect in aspects:
                print(aspect.attrib['term'] + ': ' + aspect.attrib['polarity'])

# displays all comments as per their thread level (from reddit)
def display_all_comments(comments, level):
    print((" " * level) + (">" * level) + comments.body)
    for commentReply in comments.replies:
        display_all_comments(commentReply, level + 1)
        print()

# praw setup for retrieving data from reddit.
def setup():
    reddit = praw.Reddit(client_id="7vOWHznFDrqBVA", client_secret="ExRrk05OkZat5VAYNIARhoQVS0o",
                         user_agent="windows:UniHonoursApp:v1.0.0 (by /u/Delacarpet)")
    submissionLink = input("Enter Reddit URL to perform ABSA\n")

    submission = reddit.submission(url=submissionLink)
    submission.comments.replace_more(limit=1000)

    for comment in submission.comments:
        display_all_comments(comment, 0)
