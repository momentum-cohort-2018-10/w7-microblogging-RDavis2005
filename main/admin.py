from django.contrib import admin
from main.models import Post, Comment, User

# Register your models here.

class CommentInline(admin.StackedInline):
    model = Comment
    fields = ("text",)

class PostAdmin(admin.ModelAdmin):
    list_display = ("text",)
    inlines = [
        CommentInline,
    ]

admin.site.register(User)
admin.site.register(Post, PostAdmin)