from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Posts
from django.template import loader
from django.shortcuts import render
# Create your views here.

def first_post(request):
    post = Posts.objects.first()
    ile = 5
    template = loader.get_template('posts/first.html')
    context = {'post': post,'ile': ile}
    return HttpResponse(template.render(context=context))

def posts_list(request):
    posts = Posts.objects.all()
    context = {'posts': posts}
    return render(request,"posts/list.html",context)

def post_details(request):
    posts = Posts.objects.all()
    context = {'posts': posts}
    return render(request, "posts/details.html", context)