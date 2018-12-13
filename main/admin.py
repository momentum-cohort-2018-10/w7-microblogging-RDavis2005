from django.contrib import admin
from main.models import Post, Comment, User, Following

# Register your models here.

class CommentInline(admin.StackedInline):
    model = Comment
    fields = ("text",)

class FollowersInline(admin.StackedInline):
    model = Following
    fk_name = "followed_user"
    fields = ("following_user",)

class UserAdmin(admin.ModelAdmin):
    fields = ("username", "email", "is_superuser", "is_staff", "is_active",)
    inlines = [FollowersInline]

class PostAdmin(admin.ModelAdmin):
    list_display = ("text",)
    inlines = [
        CommentInline,
    ]

admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)