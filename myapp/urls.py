from django.urls import path, include
from . import views

urlpatterns = [
  # Website related urls
  path('',views.Home.as_view(), name="home"),
  path('docs/', views.Docs.as_view(), name="docs"),
]
