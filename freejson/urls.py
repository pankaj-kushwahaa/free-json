from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.conf.urls import handler404

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('api/', include('myapi.urls')),

    # path('sitemap.xml/', views.sitemap, name='sitemap'),
    # path('robots.txt/', views.robots, name='robots'),

] 

handler404 = 'myapp.views.error_404_view'

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
