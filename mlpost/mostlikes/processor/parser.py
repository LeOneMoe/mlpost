import datetime
import requests
import json



def search(posts, posts_date):

    if type(posts) == int:

        return posts

    most_likes = 0

    for post in posts:

        post_date = datetime.datetime.fromtimestamp(post["date"])

        if ((datetime.datetime.now()) - post_date).days < posts_date:

            if post["likes"]["count"] > most_likes:
                most_likes = post["likes"]["count"]
                wall_id = post["from_id"]
                post_id = post["id"]
                post_text = post["text"]

    output_link = "https://vk.com/wall{0}_{1}".format(wall_id, post_id)

    output = json.dumps({"link": output_link,
                         "likes_count": most_likes,
                         "text": post_text
                         },
                        indent=4,
                        sort_keys=True
                        )

    return output


def getter(wall_name, posts_date):

    posts = []

    last_post = "it`s just a last post"
    last_post_date = datetime.datetime.now()

    offset = 0

    while (datetime.datetime.now() - last_post_date).days < posts_date:

        parameters = {"domain": wall_name,
                      "count": 1000000000,
                      "extended": 1,
                      "offset": offset
                      }

        try:

            temp_posts = requests.get(
                "https://api.vk.com/method/wall.get", params=parameters).json()
            temp_posts = temp_posts["response"]["wall"]
            temp_posts = temp_posts[1: len(temp_posts)]

        except KeyError:
            return 400

        posts.extend(temp_posts)

        if posts[-1] == last_post:
            break

        offset += 100

        last_post_date = datetime.datetime.fromtimestamp(posts[-1]["date"])

        last_post = posts[-1]

        return posts


def main(wall_name, posts_date):

    return search(getter(wall_name, posts_date), posts_date)
