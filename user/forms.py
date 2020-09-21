from django.contrib.auth.forms import UserCreationForm
from .models import My_User

class CreateUser(UserCreationForm):
    class Meta:
        model = My_User
        fields = ['first_name', 'last_name', 'username', 'email', 'photo']