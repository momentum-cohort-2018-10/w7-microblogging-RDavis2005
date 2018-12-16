"""microblogging URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api import views as api_views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/posts/', api_views.PostListCreateView.as_view(), name="api_post_list"),
    path('api/posts/<int:pk>/', api_views.PostRetrieveUpdateDestroyView.as_view(), name="api_post"),
    path('api/users/', api_views.UserListView.as_view(), name="api_user_list"),
    path('api/following/', api_views.FollowingListCreateView.as_view(), name="api_following_list"),
    path('api/following/<str:username>/', api_views.FollowingDestroyView.as_view(), name="api_following"),
]
