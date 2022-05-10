#!/usr/bin/python
import praw
import re
import pdb
import os
import random

reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("Knock_Knock")


#check to see if the bot has a completed posts file and creates if missing
if not os.path.isfile("completed_posts.txt"):
    completed_posts = []

#Load completed posts
else:
    with open("completed_posts.txt", "r") as f:
        completed_posts = f.read()
        completed_posts = completed_posts("\n")
        completed_posts = list(filter(None, completed_posts))

if not os.path.isfile("started_posts.txt"):
    started_posts = []

#Load started posts
else:
    with open("started_posts.txt", "r") as f1:
        started_posts = f.read()
        started_posts = started_posts("\n")
        started_posts = list(filter(None, started_posts))


for comment in subreddit.stream.comments():
    if re.search("knock knock", comment.body, re.IGNORECASE):
        comment.reply("whos there")
        print("Greg talked!")
        break





#write back to fies
with open("completed_posts.txt", "w") as f:
    for post_id in completed_posts:
        f.write(post_id + "\n")

with open("started_posts.txt", "w") as f1:
    for post_id in started_posts:
        f1.write(post_id + "\n")
