from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
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

  # JWT Authentication
  path('auth/token', TokenObtainPairView.as_view(), name="obtain_token_pair"),
  path('auth/refresh', TokenRefreshView.as_view(), name="refresh_token"),

  path('auth/posts', views.AuthBlogAPI.as_view(), name="auth_posts"),
  path('auth/posts/<int:id>', views.AuthBlogAPI.as_view(), name="auth_post-id"),
  # Comments
  path('auth/comments', views.AuthCommentAPI.as_view(), name="auth_comments"),
  path('auth/comments/<int:id>', views.AuthCommentAPI.as_view(), name="auth_comment-id"),
  
]
