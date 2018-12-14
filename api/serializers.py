from rest_framework import serializers
from main.models import Post, Comment, User

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("id", "text", "date_posted")

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(slug_field="username", read_only=True)                     #Assigns current user to Post
    comments = CommentSerializer(many=True, required=False)                                         #Turns comment id into JSON after creating a CommentSerializer
    
    class Meta:
        model = Post
        fields = ("id", "text", "owner", "comments")