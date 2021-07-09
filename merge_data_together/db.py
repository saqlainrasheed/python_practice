import sqlite3


def db_connection():
  connection = sqlite3.connect('blog.db')
  return connection


def db_create_table(connection):
  cursor = connection.cursor()
  cursor.execute("CREATE TABLE users ( \
      id INTEGER PRIMARY KEY,\
      name VARCHAR(255),\
      username VARCHAR(255), \
      email VARCHAR(255),\
      phone VARCHAR(18),\
      website VARCHAR(255)\
    )"
  )

  cursor.execute("CREATE TABLE posts (\
      id INTEGER PRIMARY KEY,\
      user_id INTEGER ,\
      title VARCHAR(255),\
      body VARCHAR(1000),\
      FOREIGN KEY(user_id) REFERENCES users(id)\
    )"
  )

  cursor.execute("CREATE TABLE comments (\
      id INTEGER PRIMARY KEY,\
      post_id INTEGER ,\
      name VARCHAR(255),\
      email VARCHAR(255),\
      body VARCHAR(255),\
      FOREIGN KEY(post_id) REFERENCES posts(id)\
    )"
  )
  connection.commit()





def insert_into_users(connection,users):
  cursor = connection.cursor()
  for user in users:
    users_details = [
        user['id'],
        user['name'],
        user['username'],
        user['email'],
        user['phone'],
        user['website']
      ]
    cursor.execute("INSERT INTO users (\
        id, name, username, email, phone, website\
      ) VALUES (?,?,?,?,?,?)",users_details)
  connection.commit()


def insert_into_posts(connection,posts):
  cursor = connection.cursor()
  for post in posts:
    post_details = [
        post['id'],
        post['userId'],
        post['title'],
        post['body']
      ]
    cursor.execute(f"INSERT INTO posts (\
        id, user_id, title, body\
      ) VALUES (?,?,?,?) ",post_details)
  connection.commit()


def insert_into_comments(connection,comments):
  cursor = connection.cursor()
  for comment in comments:
    comment_details = [
        comment['id'],
        comment['postId'],
        comment['name'],
        comment['email'],
        comment['body']
      ]
    cursor.execute(f"INSERT INTO comments (\
        id, post_id, name, email, body\
      ) VALUES (?,?,?,?,?)",comment_details)
  connection.commit()
  