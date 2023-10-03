# from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm
from apln2.models import customUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = customUser
        fields = UserCreationForm.Meta.fields+('email','phone')