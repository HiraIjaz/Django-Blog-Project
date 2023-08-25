from .models import CustomUser
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


class SignUpForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("phone", 'name', 'email', 'gender', 'age')


class UpdateUserForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('name', 'email', 'gender', 'age')
