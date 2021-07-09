import constants
import requests 

def fetch_users():
  try:
    users = requests.get(constants.BASE_URL  + constants.USERS)
    return users.json()
  except:
    return []


def fetch_posts():
  try:
    posts = requests.get(constants.BASE_URL + constants.POSTS)
    return posts.json()
  except:
    return []


def fetch_comments():
  try:
    comments = requests.get(constants.BASE_URL + constants.COMMENTS)
    return comments.json()
  except:
    return []
