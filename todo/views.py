from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, FormView
from todo.models import ToDoList, ToDoElement
from todo.forms import NewListForm, NewElementForm
from django.urls import reverse


class home(ListView):
    template_name = "todo/home.html"
    context_object_name = "todo_list"

    def get_queryset(self, **kwargs):
        return ToDoList.objects.filter()


class new_list(FormView):
    template_name = "todo/new.html"
    form_class = NewListForm
    model = ToDoList

    def form_valid(self, form):
        super(new_list, self).form_valid(form)
        form_pk = self.object.pk
        url = reverse("new", kwargs={"pk": form_pk})
        return HttpResponseRedirect(url)


class new_element(FormView):
    template_name = "todo/new.html"
    form_class = NewElementForm
    success_url = ""
    model = ToDoElement


class list_todo(DetailView):
    template_name = "todo/list.html"
    model = ToDoList

