from django.shortcuts import render
from .models import Post

# Create your views here.
def index(reqeust):
    posts = Post.objects.all()
    context = {
        'posts':posts,
    }
    return render(reqeust, 'index.html', context)