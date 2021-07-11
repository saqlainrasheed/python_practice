import sqlite3


def db_connection():
    connection = sqlite3.connect('blog.db')
    return connection


def create_table(connection):
    cursor = connection.cursor()
    cursor.execute(
        """ 
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

    cursor.execute(
        """
        CREATE TABLE post (
        id INTEGER PRIMARY KEY,
        body VARCHAR(1000),
        title VARCHAR(255),
        user_id INTEGER ,
        FOREIGN KEY(user_id) REFERENCES user(id)
        )
        """
    )

    cursor.execute(
        """
        CREATE TABLE comment (
        id INTEGER PRIMARY KEY,
        post_id INTEGER ,
        name VARCHAR(255),
        email VARCHAR(255),
        body VARCHAR(255),
        FOREIGN KEY(post_id) REFERENCES post(id)
        )
        """
    )
    connection.commit()


def insert_user(cursor, users):
    for user in users:
        cursor.execute(
            """
            INSERT INTO user (
                id, email, name, phone, username, website
            ) VALUES (
                ?, ?, ?, ?, ?, ?
            )
            """, [user]
        )


def insert_post(cursor, posts):
    for post in posts:
        print(post)
        cursor.execute(
            """
            INSERT INTO post (
                id, body, title, user_id
            ) VALUES (
                ?, ?, ?, ?
            )
            """, [post]
        )


def insert_comment(cursor, comments):
    for comment in comments:
        cursor.execute(
            """
            INSERT INTO comment (
                id, body, email, name, post_id
            ) VALUES (
                ?, ?, ?, ?, ?
            )
            """, [comment]
        )


def insert(key, data):
    connection = db_connection()
    cursor = connection.cursor()
    switch = {
        'user': lambda: insert_user(cursor, data),
        'post': lambda: insert_post(cursor, data),
        'comment': lambda: insert_comment(cursor, data),
    }

    switch.get(key, "Error: Invalid case.")
    connection.commit()
