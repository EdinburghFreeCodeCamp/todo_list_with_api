from django import forms
from django.contrib.auth.models import User

class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
	exclude = ["password", "user_permissions", "groups", "last_login", "is_superuser", "user_permissions", "is_staff", "date_joined"]

