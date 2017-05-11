from tastypie.authentication import BasicAuthentication, ApiKeyAuthentication, MultiAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie.resources import ModelResource
from .models import ToDoList, ToDoElement


class ResourceMixin(object):
    """
  	Create default settings for my resources here.

    """
    class Meta:
        authentication = MultiAuthentication(BasicAuthentication(), ApiKeyAuthentication())
        authorization = DjangoAuthorization()


class ToDoListResource(ResourceMixin, ModelResource):
    class Meta:
        queryset = ToDoList.objects.all()


class ToDoElementResource(ResourceMixin, ModelResource):
    class Meta:
        queryset = ToDoElement.objects.all()

