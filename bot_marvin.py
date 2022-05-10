#!/usr/bin/python
import praw
import re
import pdb
import os
import random

reddit = praw.Reddit('bot2')

subreddit = reddit.subreddit("Knock_Knock")

print("\nMARVBOT - Starting Marv")

#check to see if the bot has a completed posts file and creates if missing
if not os.path.isfile("completed_posts.txt"):
    completed_posts = []

#Load completed posts
else:
    with open("completed_posts.txt", "r") as f:
        completed_posts = f.read()
        completed_posts = completed_posts.split("\n")
        completed_posts = list(filter(None, completed_posts))

if not os.path.isfile("started_posts.txt"):
    started_posts = []

#Load started posts
else:
    with open("started_posts.txt", "r") as f1:
        started_posts = f1.read()
        started_posts = started_posts.split("\n")
        started_posts = list(filter(None, started_posts))



for submission in subreddit.stream.submissions(skip_existing=True):
    #make sure its not completed
    if submission.id not in started_posts:
        if re.search("joke", submission.title, re.IGNORECASE):
            submission.reply("I have very funny joke! Im so excite! \n Knock Knock")
            started_posts.append(submission.id);
            print("MARVBOT - Marv started joke")
            break

replys = 0

for comment in subreddit.stream.comments(skip_existing=True):
    if comment.author.name == reddit.user.me().name:
        continue
    if re.search("whos there", comment.body, re.IGNORECASE):
        comment.reply("poopy")
        replys += 1
        print("MARVBOT - Marv said poopy")
    if re.search("poopy who", comment.body, re.IGNORECASE):
        comment.reply("knock knock")
        replys += 1
        print("MARVBOT - Marv said knock knock)")
    if replys > 10:
        break



#write back to fies
with open("completed_posts.txt", "w") as f:
    for post_id in completed_posts:
        f.write(post_id + "\n")

with open("started_posts.txt", "w") as f1:
    for post_id in started_posts:
        f1.write(post_id + "\n")
