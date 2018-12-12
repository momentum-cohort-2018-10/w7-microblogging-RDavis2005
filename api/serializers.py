from rest_framework import serializers
from main.models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("id", "text", "date_posted")

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField() #Turns owner id into string
    comments = CommentSerializer(many=True) #Turns comment id into JSON after creating a CommentSerializer
    
    class Meta:
        model = Post
        fields = ("id", "text", "owner", "comments")