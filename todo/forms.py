from django.forms import ModelForm
from todo.models import ToDoList, ToDoElement


class NewListForm(ModelForm):
    class Meta:
        model = ToDoList
        fields = ['title']


class NewElementForm(ModelForm):
    class Meta:
        model = ToDoElement
        fields = ["title"]
