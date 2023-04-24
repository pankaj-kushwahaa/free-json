from django.urls import path, include
from . import views

urlpatterns = [
  # Posts
  path('posts', views.BlogAPI.as_view(), name="posts"),
  path('posts/<int:id>', views.BlogAPI.as_view(), name="post-id"),
  # Comments
  path('comments', views.CommentAPI.as_view(), name="comments"),
  path('comments/<int:id>', views.CommentAPI.as_view(), name="comment-id"),
  # Users
  path('users', views.UserAPI.as_view(), name="users"),
  path('users/<int:id>', views.UserAPI.as_view(), name="user-id"),
]
