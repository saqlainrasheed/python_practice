import json
import db
import fetch
import merge


def main():
  users = fetch.fetch_users()
  posts = fetch.fetch_posts()
  comments = fetch.fetch_comments()
  post_comments = merge.add_comments_in_posts(posts, comments)
  data = merge.add_posts_in_users(users, post_comments)

  with open("data.json", "w") as output_file:
    json.dump(data, output_file)

  connection = db.db_connection()
  db.create_table(connection)
  db.insert_user(connection, users)
  db.insert_post(connection, posts)
  db.insert_comment(connection, comments)


main()
