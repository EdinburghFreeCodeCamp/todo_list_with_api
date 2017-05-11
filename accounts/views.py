from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView
from .forms import EditUserForm
import logging
# Create your views here.

class profile(TemplateView):
    template_name = "accounts/profile.html"

    def get_context_data(self, *args, **kwargs):
        c = super(profile, self).get_context_data(*args, **kwargs)
        c["user"] = self.request.user
        c["apikey"] = "1234"
        c["edit_form"] = EditUserForm(instance=self.request.user)
        return c

    def post(self, *args, **kwargs):
        form = EditUserForm(self.request.POST, instance=self.request.user)
        if form.is_valid():
            form.save()
	    return redirect(reverse("profile"))
	return form
