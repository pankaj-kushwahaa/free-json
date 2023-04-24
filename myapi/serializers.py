from rest_framework import serializers
from myapp.models import User, Blog, Comment
from pprint import pprint

class UserSerializer(serializers.ModelSerializer):
  userId = serializers.SerializerMethodField('user_id')
  def user_id(self, obj):
    return obj.id
  class Meta:
    model = User
    fields = ['userId', 'username']

class CommentSerializer(serializers.ModelSerializer): 
  class Meta:
    model = Comment
    fields = ['commentId', 'postId', 'comment', 'name', 'email']

class BlogSerializer(serializers.ModelSerializer):
  user = UserSerializer(source='userId', read_only=True)
  comments = serializers.SerializerMethodField('comments_all', read_only=True)

  def comments_all(self, obj):
    comments = Comment.objects.filter(postId=obj.postId)
    serializer = CommentSerializer(comments, many=True)
    return serializer.data
    
  class Meta:
    model = Blog
    fields = ['postId', 'title', 'description', 'user', 'comments']

'''
    commentId = IntegerField(label='CommentId', read_only=True)
    postId = PrimaryKeyRelatedField(allow_null=True, label='PostId', queryset=Blog.objects.all(), required=False)
    comment = CharField(max_length=500)
    name = CharField(max_length=150)
    email = CharField(allow_null=True, max_length=100, required=False)
'''