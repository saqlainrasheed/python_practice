import sqlite3


def db_connection():
  connection = sqlite3.connect("blog.db")
  return connection


# def insert(connection, data):
#   cursor = connection.cursor()
  

#   switcher.get(data,)

#   connection.commit()


def create_table(connection):
  cursor = connection.cursor()
  cursor.execute(""" 
    CREATE TABLE user ( 
      id INTEGER PRIMARY KEY,
      email VARCHAR(255),
      name VARCHAR(255),
      phone VARCHAR(18),
      username VARCHAR(255),
      website VARCHAR(255)
    ) 
  """
  )

  cursor.execute("""
    CREATE TABLE post (
      id INTEGER PRIMARY KEY,
      body VARCHAR(1000),
      title VARCHAR(255),
      user_id INTEGER ,
      FOREIGN KEY(user_id) REFERENCES users(id)
    )
  """
  )

  cursor.execute("""
    CREATE TABLE comment (
      id INTEGER PRIMARY KEY,
      post_id INTEGER ,
      name VARCHAR(255),
      email VARCHAR(255),
      body VARCHAR(255),
      FOREIGN KEY(post_id) REFERENCES posts(id)
    )
  """
  )
  connection.commit()


def insert_user(connection, users):
  cursor = connection.cursor()
  for user in users:
    cursor.execute("""
      INSERT INTO user (
        id, email, name, phone, username, website
      ) VALUES (
        ?, ?, ?, ?, ?, ?
      )
      """,[
        user["id"],
        user["email"],
        user["name"],
        user["phone"],
        user["username"],
        user["website"],
      ]
    )
  connection.commit()


def insert_post(connection, posts):
  cursor = connection.cursor()
  for post in posts: 
    cursor.execute("""
      INSERT INTO post (
        id, body, title, user_id,
      ) VALUES (
        ?, ?, ?, ?
      )
      """,[
        post["id"], 
        post["body"],
        post["title"], 
        post["userId"], 
      ]
    )
  connection.commit()


def insert_comment(connection, comments):
  cursor = connection.cursor()
  for comment in comments:
    cursor.execute("""
      INSERT INTO comment (
        id, body, email, name, post_id
      ) VALUES (
        ?, ?, ?, ?, ?
      )
      """,[
        comment["id"],
        comment["body"],
        comment["email"],
        comment["name"],
        comment["postId"],
      ]
    )
  connection.commit()