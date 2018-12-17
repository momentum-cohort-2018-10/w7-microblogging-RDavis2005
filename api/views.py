from main.models import Post, Following, User
from api.serializers import PostSerializer, FollowingSerializer, UserSerializer, CommentSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from django.shortcuts import get_object_or_404

# Create your views here.

class PostListCreateView(APIView):                                              #Allows user ability to see all posts
    def get(self, request):
        posts = Post.objects.filter(owner=request.user)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):                                                    #Allows user to create a new post
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)                                 #Turns data into actual book object
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)

class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):     #Allows user ability to get, update or destroy a post
    serializer_class = PostSerializer

    def get_queryset(self):
        return self.request.user.posts

class CommentCreateView(generics.CreateAPIView):                               #Allows user ability to create a new comment
    serializer_class = CommentSerializer

    def perform_create(self, serializer):                                       #Finds a particular post by pk if it exists and returns it
        post = get_object_or_404(Post, pk=self.kwargs["post_pk"])
        serializer.save(post=post)

class FollowingListCreateView(APIView):                                         #Allows user to see a list of followed users
    def get(self, request):
        followings = Following.objects.filter(following_user=request.user)
        serializer = FollowingSerializer(followings, many=True)
        return Response(serializer.data)

    def post(self, request):                                                    #Allows user to create a new followed user
        serializer = FollowingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)                                 #Turns data into actual book object
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)

class FollowingDestroyView(generics.DestroyAPIView):                            #Allows user ability to delete followed users by username
    serializer_class = FollowingSerializer
    lookup_field = "followed_user__username"
    lookup_url_kwarg = "username"

    def get_queryset(self):                                                     #Creates a query by that particular username and returns it
        return self.request.user.follows_from

class UserListView(generics.ListAPIView):                                       #Allows admin ability to see a list of all users
    serializer_class =  UserSerializer
    queryset = User.objects.all()