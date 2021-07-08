# fetch all the data and combine it all together and then store it on the local file

import json
from sqlite3.dbapi2 import Connection
import requests
import sqlite3

connection = sqlite3.connect('blog_data.db')
cursor = connection.cursor()


def fetch_users():
  try:
    fetched_users_data = requests.get('https://jsonplaceholder.typicode.com/users')
    return fetched_users_data.json()
  except:
    return 'Unable to fetch the data...'


def fetch_posts():
  try:
    fetched_posts_data = requests.get('https://jsonplaceholder.typicode.com/posts')
    return fetched_posts_data.json()
  except:
    return 'Unable to fetch the data...'


def fetch_comments():
  try:
    fetched_comments = requests.get('https://jsonplaceholder.typicode.com/comments')
    return fetched_comments.json()
  except:
    return 'Unable to fetch the data...'



# Filtering posts and adding them up in the users data as key

def add_posts_as_key_in_users(users,posts):
  for user in users:
    user['posts'] = filter_posts_against_user_id(user['id'],posts)
  return users

def filter_posts_against_user_id(user_id,fetched_posts):
  posts = []
  for post in fetched_posts:
    if post['userId'] == user_id:
      posts.append(post)
  return posts


#filtering comments against postId and then adding them up in the post data


def add_comments_as_key_in_posts(posts,comments):
  for post in posts:
    post['comments'] = filter_comments_against_post_id(post['id'],comments)
  return posts


def filter_comments_against_post_id(post_id,fetched_comments):
  comments = []
  for comment in fetched_comments:
    if comment['postId'] == post_id:
      comments.append(comment)
  return comments




def main():
  users = fetch_users()
  posts = fetch_posts()
  comments = fetch_comments()
  commented_posts = add_comments_as_key_in_posts(posts,comments)
  with open('data.json', 'w') as output_file:
    json.dump(add_posts_as_key_in_users(users,commented_posts), output_file)


main()