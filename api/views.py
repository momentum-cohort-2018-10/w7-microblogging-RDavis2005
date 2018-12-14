from django.shortcuts import render
from main.models import Post
from api.serializers import PostSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(["GET", "POST"])                              #If request is a GET, show user's post list
def post_create_or_list(request):                       #If request is a POST, create a new post
    if request.method == "POST":
        return create_post(request)
    return post_list(request)


def create_post(request):                               #Create a new post using the Post model
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(owner=request.user)
        return Response(serializer.data, status=201)

    return Response(serializer.errors, status=400)

def post_list(request):                                 #Retrieve user's list of posts
    posts = Post.objects.filter(owner=request.user)
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)