from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [
    path('', views.show_blogpost_list, name='blogpost_list'),
    path('admin/', admin.site.urls),
]
