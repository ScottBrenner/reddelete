import logging
import praw
import os

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def run(event, context):
  reddit = praw.Reddit(user_agent='reddelete',
    client_id=os.environ['REDDIT_CLIENT_ID'],
    client_secret=os.environ['REDDIT_CLIENT_SECRET'],
    username=os.environ['REDDIT_USERNAME'],
    password=os.environ['REDDIT_PASSWORD'])
  for comment in reddit.redditor(os.environ['REDDIT_USERNAME']).comments.new(limit=None):
    if (comment.score < int(os.environ['DELETE_THRESHOLD'])):
      comment.delete()
      logger.info("Deleted: " + comment.id)