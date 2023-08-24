from .models import CustomUser
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


class signUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("phone", 'name', 'email', 'gender', 'age')


class updateUserForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('name', 'email', 'gender', 'age')
