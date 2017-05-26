from django.shortcuts import render
import requests
import json
import datetime


# Create your views here.

def IndexView(request):
    print(request.GET['id'])
    print(request.GET['time'])
    return render(request, "index.html", locals())


def MLPostView(request):

    wall_name = request.GET["id"]
    posts_date = int(request.GET["time"])

    posts = requests.get(
        "https://api.vk.com/method/wall.get?domain={0}&count=10000&extended=1".format(wall_name)).text
    posts = json.loads(posts)["response"]["wall"]
    posts = posts[1: len(posts)]

    most_likes = 0

    for post in posts:

        if ((datetime.datetime.now()) - datetime.datetime.fromtimestamp(post["date"])).days < posts_date:

            if post["likes"]["count"] > most_likes:
                most_likes = post["likes"]["count"]
                wall_id = post["from_id"]
                post_id = post["id"]
                post_date = datetime.datetime.fromtimestamp(post["date"])

                output_link = "https://vk.com/wall{0}_{1}".format(wall_id, post_id)

    output = json.dumps({"link": output_link, "likes_count": most_likes})

    return render(request, "index.html", locals())
