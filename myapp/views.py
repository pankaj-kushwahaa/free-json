from django.shortcuts import render
from django.views import View


class Home(View):
  def get(self, request):
    # url = 'https://jsonplaceholder.typicode.com/comments'
    # res = requests.get(url)
    # data = json.loads(res.text)
    # pprint(data)
    # Create User
    # for i in range(1, 11):
    #   user = User.objects.create_user(f"user{i}", password= "Dera@123")
    #   user.save()
    # translator = Translator()
    # for i in data:
    #   user = User.objects.get(id=i.get('userId'))
    #   title = translator.translate(i.get('title')).text
    #   desc = translator.translate(i.get('body')).text
    #   Blog.objects.create(title=title, description=desc, userId=user)

      # postId = Blog.objects.get(postId=i.get('postId'))
      # name = translator.translate(i.get('name')).text
      # email = translator.translate(i.get('email')).text
      # comment = translator.translate(i.get('body')).text
      # Comment.objects.create(comment=comment, name=name, email=email, postId=postId)
    return render(request, 'myapp/home.html')
  
class Docs(View):
  def get(self, request):
    data = dict(url=request.build_absolute_uri("/"))
    return render(request, 'myapp/docs.html', data)
  
def error_404_view(request, exception):
  return render(request, 'myapp/error.html')


