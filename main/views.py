from django.shortcuts import render
from main.models import Post

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        posts = request.user.posts.all()
        return render(request, "main/post_list.html", {"posts": posts})
    else:
        return render(request, "main/not_logged_in.html")