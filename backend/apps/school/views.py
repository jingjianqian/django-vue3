import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.http import require_http_methods

from school.models import Student
from utils import serializers


@require_http_methods(["GET"])
def show_students(request):
    response = {}

    try:

        students = Student.objects.filter()

        response['list'] = json.loads(serializers.serialize("json", students))

        response['msg'] = 'success'

        response['error_num'] = 0

    except Exception as e:

        response['msg'] = str(e)

        response['error_num'] = 1

    # return JsonResponse(response, content_type='application/json,charset=utf-8')
    return HttpResponse(json.dumps(response, ensure_ascii=False), content_type='application/json')
