from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Posts
from django.template import loader
from django.shortcuts import render
# Create your views here.

def post_details(request,post_id):
    post = Posts.objects.get(pk=post_id)
    return render(request,"posts/details.html",{'post':post})

def posts_list(request):
    posts = Posts.objects.all()
    context = {'posts': posts}
    return render(request,"posts/list.html",context)