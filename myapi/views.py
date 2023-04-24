from django.shortcuts import HttpResponse
from myapp.models import Blog, Comment, User
from .serializers import BlogSerializer, CommentSerializer, UserSerializer
from rest_framework.views import APIView
from django.views import View
from rest_framework.response import Response
from rest_framework import status
import json


class BlogAPI(APIView):
  def get(self, request, id=None, format=None):
    if id is not None:
      id = id
      stu = Blog.objects.get(postId=id)
      serializer = BlogSerializer(stu)
      return Response(serializer.data, status=status.HTTP_200_OK)
    stu = Blog.objects.all()
    serializer = BlogSerializer(stu, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

  def post(self, request, format=None):
    pythondata = request.data
    serializer = BlogSerializer(data=pythondata)
    data = dict()
    data['postId'] = 101
    for i in serializer.initial_data:
      data[i] = serializer.initial_data.get(i)
    # print(data)
    if serializer.is_valid():
      data['message'] = 'Data Created.!!'
      return Response(data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def put(self, request, id=None, format=None):
    try:
      stu = Blog.objects.get(postId=id)
      serializer = BlogSerializer(stu, data=request.data)
      data = dict()
      data['postId'] = id
      for i in serializer.initial_data:
        data[i] = serializer.initial_data.get(i)
      if serializer.is_valid():
        # serializer.save()
        for i in serializer.data:
          if data.get(i) is None:
            data[i] = serializer.data.get(i)
          data['message'] = 'Data Updated Successfully..!!'
        return Response(data, status=status.HTTP_202_ACCEPTED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except:
      data = dict(message='postId does not exists, please enter postId between 1 to 100')
      return Response(data,  status=status.HTTP_404_NOT_FOUND)

  def patch(self, request, id=None, format=None):
    try:
      stu = Blog.objects.get(postId=id)
      serializer = BlogSerializer(stu, data=request.data, partial=True)
      data = dict()
      data['postId'] = id
      for i in serializer.initial_data:
        data[i] = serializer.initial_data.get(i)
      if serializer.is_valid():
        for i in serializer.data:
          if data.get(i) is None:
            data[i] = serializer.data.get(i)
          data['message'] = 'Data Updated Successfully..!!'
        return Response(data, status=status.HTTP_202_ACCEPTED)
      return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    except:
      data = dict(message='postId does not exists, please enter postId between 1 to 100')
      return Response(data)

  def delete(self, request, id=None, format=None):
    try:
      stu = Blog.objects.get(postId=id)
      data = request.data
      data['message'] = 'Data Deleted.!!'
      data['postId'] = id
      return Response(data)
    except:
      data = dict(message="postId is not valid..")
      return Response(data,  status=status.HTTP_404_NOT_FOUND)


class CommentAPI(APIView):
  def get(self, request, id=None, format=None):
    if id is not None:
      stu = Comment.objects.get(commentId=id)
      serializer = CommentSerializer(stu, context={"request":request})
      return Response(serializer.data, status=status.HTTP_200_OK)
    stu = Comment.objects.all()
    serializer = CommentSerializer(stu, many=True, context={"request":request})
    return Response(serializer.data, status=status.HTTP_200_OK)

  def post(self, request, format=None):
    pythondata = request.data
    serializer = CommentSerializer(data=pythondata)
    data = dict()
    data['commentId'] = 101
    for i in serializer.initial_data:
      data[i] = serializer.initial_data.get(i)
    # print(data)
    if serializer.is_valid():
      data['postId'] = serializer.data.get('postId')
      data['message'] = 'Data Created.!!'
      return Response(data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def put(self, request, id=None, format=None):
    try:
      stu = Comment.objects.get(commentId=id)
      serializer = CommentSerializer(stu, data=request.data)
      data = dict()
      data['commentId'] = id
      for i in serializer.initial_data:
        data[i] = serializer.initial_data.get(i)
      # print(data)
      if serializer.is_valid():
        for i in serializer.data:
          if data.get(i) is None:
            data[i] = serializer.data.get(i)
            data['message'] = 'Data Updated Successfully.!!'
        return Response(data, status=status.HTTP_202_ACCEPTED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except:
      data = dict(message='commentId does not exists, please enter commentId between 1 to 100')
      return Response(data, status=status.HTTP_400_BAD_REQUEST)

  def patch(self, request, id=None, format=None):
    try:
      print(id, type(id))
      stu = Comment.objects.get(commentId=id)
      serializer = CommentSerializer(stu, data=request.data, partial=True)
      print(serializer)
      data = dict()
      data['commentId'] = id
      for i in serializer.initial_data:
        data[i] = serializer.initial_data.get(i)
      # print(data)
      print(serializer.is_valid())
      if serializer.is_valid():
        for i in serializer.data:
          if data.get(i) is None:
            data[i] = serializer.data.get(i)
          data['message'] = 'Data Updated Successfully.!!'
        return Response(data, status=status.HTTP_202_ACCEPTED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except:
      data = dict(message='CommentId does not exists, please enter commentId between 1 to 500')
      return Response(data, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, id=None, format=None):
    try:
      stu = Blog.objects.get(postId=id)
      data = request.data
      data['message'] = 'Data Deleted.!!'
      data['commentId'] = id
      return Response(data)
    except:
      data = dict(message="commentId is not valid...")
      return Response(data,  status=status.HTTP_404_NOT_FOUND)


class UserAPI(View):
  def get(self, request, id=None):
    try:
      if id is not None:
        stu = User.objects.get(id=id)
        user = User.objects.filter(id=id).values('id', 'username')
        blog = Blog.objects.filter(userId=stu).values('postId', 'title', 'description', 'userId')
        data = dict(user=list(user), post=list(blog))
        data = json.dumps(data)
        return HttpResponse(data, content_type='application/json', status=status.HTTP_200_OK, charset="utf-8")
      stu = User.objects.all()
      li = list()
      for i in stu:
        di = dict()
        blog = Blog.objects.filter(userId=i).values('postId', 'title', 'description', 'userId')
        di['userId'] = i.id
        di['username'] = i.username
        l = [j for j in blog]
        di['posts'] = list(l)
        li.append(di)
      data = json.dumps(li)
      return HttpResponse(data, status=status.HTTP_200_OK, content_type='application/json')
    except:
      return HttpResponse(json.dumps(dict(message="userId is not valid, please provide userdId between the range 1 to 10")), status=status.HTTP_404_NOT_FOUND)
