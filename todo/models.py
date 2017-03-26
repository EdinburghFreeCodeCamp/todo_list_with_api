from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class ToDoElement(models.Model):
    status_choices=(
        (0, "not started"),
        (1, "started"),
        (2, "on hold"),
        (3, "finished")
    )
    status = models.IntegerField(choices=status_choices)
    title = models.CharField(max_length=100)
    order = models.IntegerField()


class ToDoList(models.Model):
    title = models.CharField(max_length=100)
    elements = models.ManyToManyField(ToDoElement)
    user = models.ForeignKey(User)

    def percentage_complete(self):
        fTasks = self.elements.filter(status=3)
        f = fTasks.count()
        e = self.elements.all().count()
        return float(f) / float(e)
