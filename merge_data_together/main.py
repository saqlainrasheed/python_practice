import json
import db
import fetch
from merge import merge
from urls import USERS_URL, POSTS_URL, COMMENTS_URL


def main():
    users = fetch.get(USERS_URL)
    posts = fetch.get(POSTS_URL)
    comments = fetch.get(COMMENTS_URL)
    data = merge(users, posts, comments)

    with open('data.json', 'w') as output_file:
        json.dump(data, output_file)

    connection = db.db_connection()
    db.create_table(connection)
    db.insert('user', users)
    db.insert('post', posts)
    db.insert('comment', comments)


main()
