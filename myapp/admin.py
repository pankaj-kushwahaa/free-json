from django.contrib import admin
from .models import Blog, Comment

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
  list_display = ['postId', 'title',  'description', 'userId']
                  
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
  list_display = ['commentId', 'postId', 'comment', 'name', 'email']
