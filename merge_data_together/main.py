import json
import db
import fetch
import merge

def main():
  users = fetch.fetch_users()
  posts = fetch.fetch_posts()
  comments = fetch.fetch_comments()
  commented_posts = merge.add_comments_in_posts(posts,comments)
  joined_data = merge.add_posts_in_users(users,commented_posts)
  
  with open('data.json', 'w') as output_file:
    json.dump(joined_data, output_file)

  connection = db.db_connection()
  db.db_create_table(connection)
  db.insert_into_users(connection,users)
  db.insert_into_posts(connection,posts)
  db.insert_into_comments(connection, comments)



main()