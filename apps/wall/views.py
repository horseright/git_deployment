from django.shortcuts import render, redirect
from .models import Blog, Comment

def index(request):
    context = {
    'blogs': Blog.objects.all()
    }
    return render(request, 'wall/index.html', context)

def blogs(request):
    Blog.objects.create(title=request.POST['title'], blog=request.POST['blog'])
    return redirect('/')

def comments(request, id):
    blog=Blog.objects.get(id=id)
    Comment.objects.create(comment=request.POST['comment'], blog=blog)
    return redirect('/')
