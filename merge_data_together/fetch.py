import constants
import requests 

def fetch_users():
  users = requests.get(constants.USERS_URL)
  return users.json()


def fetch_posts():
  posts = requests.get(constants.POSTS_URL)
  return posts.json()
  

def fetch_comments():
  comments = requests.get(constants.COMMENTS_URL)
  return comments.json()