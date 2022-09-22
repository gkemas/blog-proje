from ast import Return
from multiprocessing import context
from django.shortcuts import render
from .models import Post


def post_list(request):
    qs = Post.objects.all()
    context ={
        "object_list":qs
    }
    return render (request,"blog/post_list.html",context)
