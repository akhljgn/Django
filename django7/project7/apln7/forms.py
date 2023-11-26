from django import forms
from apln7.models import login

class loginForm(forms.ModelForm):
    class Meta:
        model = login
        fields = '__all__'