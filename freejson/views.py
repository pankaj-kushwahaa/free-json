from django.shortcuts import HttpResponse, render

def sitemap(request):
  f = open('myapp/sitemap.xml')
  content = f.read()
  f.close()
  return HttpResponse(content, content_type="application/xml")

def robots(request):
  f = open('myapp/robots.txt', 'r')
  file_content = f.read()
  f.close()
  return HttpResponse(file_content, content_type="text/plain")
