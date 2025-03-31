from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

# Create your views here.
def index(reqeust):
    posts = Post.objects.all()
    context = {
        'posts':posts,
    }
    return render(reqeust, 'index.html', context)

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:index')
    else:
        form = PostForm()

    context = {
        'form' : form
    }
    return render(request, 'create.html', context)