from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.models import signals
from tastypie.models import create_api_key, ApiKey
from django.urls import reverse
from django.views.generic import TemplateView
from .forms import EditUserForm
import logging
from django.utils import timezone

# Create your views here.

class profile(TemplateView):
    template_name = "accounts/profile.html"

    def get_context_data(self, *args, **kwargs):
        c = super(profile, self).get_context_data(*args, **kwargs)
        c["user"] = self.request.user
        try:
        	c["apikey"] =  ApiKey.objects.get(user=self.request.user).key
	except:
		c["apikey"] = "not set. Please generate to use locally."
        c["edit_form"] = EditUserForm(instance=self.request.user)
        return c

    def post(self, *args, **kwargs):
        form = EditUserForm(self.request.POST, instance=self.request.user)
        if form.is_valid():
            form.save()
	    return redirect(reverse("profile"))
	return form


def generate_api_key(request):
    api_key, _ = ApiKey.objects.get_or_create(user=request.user)
    api_key.key = api_key.generate_key()
    api_key.created = timezone.now() 
    api_key.save()
    return redirect(reverse("profile"))
