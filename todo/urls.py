from django.conf.urls import url
import views as todo_views


urlpatterns = [
    url('new', todo_views.new_list.as_view()),
    url('new/(?P<pk>[0-9]+)', todo_views.new_element.as_view()),
    url(r'(?P<pk>[0-9]+)', todo_views.list_todo.as_view()),
    url('^', todo_views.home.as_view()),
]
