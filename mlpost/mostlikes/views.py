from django.http import HttpResponse
from .processor import parser_
from django.utils.datastructures import MultiValueDictKeyError
from django.shortcuts import render
import json

# Create your views here.

def IndexView(request):
    output = "HELLO"
    return render(request, "index.html", locals())


def MLPostView(request):

    try:
        wall_name = request.GET["id"]
        posts_date = int(request.GET["days"])

    except MultiValueDictKeyError:
        output = json.dumps({"error":"Не введены или отсутствуют входные данные, попробуйте: "
                            "http://127.0.0.1:8000/api/mlpost?id={идентификатор стены}ch&days={кол-во дней}"},
                            indent=4, sort_keys=True)
        return HttpResponse(output, content_type="application/json", status=400)

    return HttpResponse(parser_.main(wall_name, posts_date), content_type="application/json", status=200)



"""posts = requests.get(
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
                post_text = post["text"]

    output_link = "https://vk.com/wall{0}_{1}".format(wall_id, post_id)

    output = json.dumps({"link": output_link, "likes_count": most_likes, "text": str(post_text)},
                        indent=4, sort_keys=True)

    return HttpResponse(output, content_type="application/json")"""