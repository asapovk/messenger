from django.shortcuts import render
from django.http import JsonResponse
from .models import *

def comments_list(request):
    result = []
    for each_comment in comment.objects.all():
        result.append({ 'user': each_comment.user, 'text': each_comment.text })
    return JsonResponse(result, safe=False)

def comment_id(request, id):
    result = []
    this_comment = comment.objects.get(pk= id)
    result.append({ 'user': this_comment.user, 'text': this_comment.text })
    return JsonResponse(result, safe=False)