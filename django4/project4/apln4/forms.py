from django.contrib.auth.forms import UserCreationForm
from apln4.models import CustUser

class CustUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustUser
        fields = UserCreationForm.Meta.fields+('first_name','last_name','email','phone',)