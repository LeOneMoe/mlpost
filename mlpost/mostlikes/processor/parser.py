import datetime
import requests
import json



def search(posts, posts_date):

    if posts == -1:

        return -1

    most_likes = 0

    for post in posts:

        if ((datetime.datetime.now()) - datetime.datetime.fromtimestamp(post["date"])).days < posts_date:

            if post["likes"]["count"] > most_likes:
                most_likes = post["likes"]["count"]
                wall_id = post["from_id"]
                post_id = post["id"]
                post_text = post["text"]

    output_link = "https://vk.com/wall{0}_{1}".format(wall_id, post_id)

    output = json.dumps({"link": output_link, "likes_count": most_likes, "text": post_text},
                                    indent=4, sort_keys=True)

    return output


def getter(wall_name):

    try:
        posts = requests.get(
            "https://api.vk.com/method/wall.get?domain={0}&count=10000&extended=1".format(wall_name)
        ).text
        posts = json.loads(posts)["response"]["wall"]
        posts = posts[1: len(posts)]

        return posts

    except KeyError:

        return -1


def main(wall_name, posts_date):

    return search(getter(wall_name), posts_date)
