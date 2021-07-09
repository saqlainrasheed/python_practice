
def add_posts_in_users(users,posts):
  for user in users:
    user['posts'] = get_posts(user['id'],posts)
  return users


def get_posts(user_id,posts):
  filtered_posts = []
  for post in posts:
    if post['userId'] == user_id:
      filtered_posts.append(post)
  return filtered_posts



def add_comments_in_posts(posts,comments):
  for post in posts:
    post['comments'] = get_comments(post['id'],comments)
  return posts


def get_comments(post_id,comments):
  filtered_comments = []
  for comment in comments:
    if comment['postId'] == post_id:
      filtered_comments.append(comment)
  return filtered_comments

