# fetch all the data and combine it all together and then store it on the local file

import json
import requests
import sqlite3
from sqlite3 import Error

from requests.api import post

#database connection
def sql_connection():
  try:
    connection = sqlite3.connect('blog.db')
    return connection
  except Error:
    print(Error)


def sql_tables_creation(connection):
  cursor = connection.cursor()
  #creating user table
  cursor.execute("CREATE TABLE users(id integer PRIMARY KEY,name varchar(255), username varchar(255), email varchar(255),phone varchar(255), website varchar(255))")

  #creating posts table
  cursor.execute("CREATE TABLE posts(id integer PRIMARY KEY, userId integer , title varchar(255), body varchar(255),FOREIGN KEY(userId) REFERENCES users(id) )")

  #creating comments table
  cursor.execute("CREATE TABLE comments(id integer PRIMARY KEY, postId integer , name varchar(255), email varchar(255), body varchar(255),FOREIGN KEY(postId) REFERENCES posts(id))")
  connection.commit()



#users table insertion
def inserting_data_into_users_table(connection,users_data_list):
  cursor = connection.cursor()
    #looping through every user so we can insert it into db
  for user in users_data_list:
    cursor.execute('INSERT INTO users(id, name, username, email, phone, website) VALUES(?, ?, ?, ?, ?, ?)', [user['id'],user['name'],user['username'],user['email'],user['phone'],user['website']])
  connection.commit()


def inserting_data_into_posts_table(connection,posts_data_list):
  cursor = connection.cursor()
  #looping through every post so we can insert it into db
  for post in posts_data_list:
    cursor.execute('INSERT INTO posts(id, userId, title, body) VALUES(?, ?, ?, ?)', [post['id'],post['userId'],post['title'],post['body']])
  connection.commit()



def inserting_data_into_comments_table(connection,comments_data_list):
  cursor = connection.cursor()
    #looping through every comment so we can insert it into db
  for comment in comments_data_list:
    cursor.execute('INSERT INTO comments(id, postId, name, email, body) VALUES(?, ?, ?, ?, ?)', [comment['id'],comment['postId'],comment['name'],comment['email'],comment['body']])
  connection.commit()
  




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
  joined_data = add_posts_as_key_in_users(users,commented_posts)
  
  with open('data.json', 'w') as output_file:
    json.dump(joined_data, output_file)

  #sql table creation and data insertion
  connection = sql_connection()
  sql_tables_creation(connection)
  inserting_data_into_users_table(connection,users)
  inserting_data_into_posts_table(connection,posts)
  inserting_data_into_comments_table(connection, comments)



main()