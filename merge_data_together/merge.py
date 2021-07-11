def add_posts_in_users(users, posts):
    for user in users:
        user['posts'] = get_posts(user['id'], posts)
    return users


def get_posts(user_id, posts):
    user_posts = []
    for post in posts:
        if post['userId'] == user_id:
            user_posts.append(post)
    return user_posts


def add_comments_in_posts(posts, comments):
    for post in posts:
        post['comments'] = get_comments(post['id'], comments)
    return posts


def get_comments(post_id, comments):
    post_comments = []
    for comment in comments:
        if comment['postId'] == post_id:
            post_comments.append(post_comments)
    return post_comments


def merge(users, posts, comments):
    post_comments = add_comments_in_posts(posts, comments)
    data = add_posts_in_users(users, post_comments)
    return data
