from django.contrib import admin
from .models import ToDoElement, ToDoList
# Register your models here.


class ToDoElementAdmin(admin.ModelAdmin):
    fields = ("title", "status", "todolist_set")
    list_display = ("title", "status", "todolist_set")
    readonly_fields = ("todolist_set", )

    def todolist_set(self, obj):
        return [n.title for n in obj.todolist_set.all()]


class ToDoListAdmin(admin.ModelAdmin):
    fields = ("title", "percentage" )
    list_display = ("title", "percentage" )
    readonly_fields = ("percentage",)

    def percentage(self, obj):
        return str(obj.percentage_complete() * 100) + "%"

admin.site.register(ToDoElement, ToDoElementAdmin)
admin.site.register(ToDoList, ToDoListAdmin)
