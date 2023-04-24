from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Blog(models.Model):
  postId = models.BigAutoField(primary_key=True, auto_created=True)
  title = models.CharField(max_length=200)
  description = models.TextField()
  userId = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

  def __str__(self) -> str:
    return self.title
  


class Comment(models.Model):
  commentId = models.BigAutoField(primary_key=True)
  postId = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)
  comment = models.CharField(max_length=500)
  name = models.CharField(max_length=150)
  email = models.CharField(max_length=100, null=True)
 
  def __str__(self) -> str:
    return self.comment


