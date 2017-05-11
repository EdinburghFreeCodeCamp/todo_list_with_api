"""todo_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import urls as auth_urls
from todo_website.views import homepage
from tastypie.api import Api
from todo import api as todo_api

v1_api = Api(api_name='v1')
v1_api.register(todo_api.ToDoListResource())
v1_api.register(todo_api.ToDoElementResource())


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^todo/', include('todo.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^api/', include(v1_api.urls)),
    url(r'^$', homepage.as_view()),
    url('', include(auth_urls)),
]
