from django.http import HttpResponse
from .processor import parser
from django.utils.datastructures import MultiValueDictKeyError
from django.shortcuts import render
import json


NO_CONTENT = "Не введены входные данные, попробуйте: " \
             "http://127.0.0.1:8000/api/mlpost?id={идентификатор стены}ch&days={кол-во дней}"
INVALID_CONTENT = "Введены непрвильные данные"

NO_CONTENT_CODE = 204
INVALID_CONTENT_CODE = 400
OK_CODE = 200


def IndexView(request):
    output = "HELLO"
    return render(request, "index.html", locals())


def MLPostView(request):

    try:
        wall_name = request.GET["id"]
        posts_date = int(request.GET["days"])

    except MultiValueDictKeyError:
        output = json.dumps(
            {"error": NO_CONTENT},
            indent=4,
            sort_keys=True
        )

        return HttpResponse(output, content_type="application/json", status=NO_CONTENT_CODE)

    if parser.main(wall_name, posts_date) == -1:
        output = json.dumps(
            {"error": INVALID_CONTENT},
            indent=4,
            sort_keys=True
        )

        return HttpResponse(output, content_type="application/json", status=INVALID_CONTENT_CODE)

    return HttpResponse(parser.main(wall_name, posts_date), content_type="application/json", status=OK_CODE)
