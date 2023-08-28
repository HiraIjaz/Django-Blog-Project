from .models import CustomUser
from django.contrib.auth.forms import forms, UserChangeForm, UserCreationForm


class SignUpForm(UserCreationForm):
    """
    Form for user registration.

    Inherits from UserCreationForm and adds additional fields for user registration.

    Attributes:
        Meta:
            model (CustomUser): The user model to be used.
            fields (tuple): Fields to be included in the form.

    Methods:
        clean_age: Custom validation for user age.

    """

    class Meta:
        model = CustomUser
        fields = ('phone', 'name', 'email', 'gender', 'age')

    def clean_age(self):
        """
        Custom validation for user age.

        Returns:
            int: Validated age.

        Raises:
            forms.ValidationError: If age is too young or too old for the community.
        """
        age = self.cleaned_data.get('age')
        if age < 15:
            raise forms.ValidationError('You are too young to be a part of the community')
        elif age > 80:
            raise forms.ValidationError("You are too old to be a part of the community")
        return age


class UpdateUserForm(UserChangeForm):
    """
    Form for updating user information.

    Inherits from UserChangeForm and provides fields for updating user information.

    Attributes:
        Meta:
            model (CustomUser): The user model to be used.
            fields (tuple): Fields to be included in the form.
    """

    class Meta:
        model = CustomUser
        fields = ('name', 'email', 'gender', 'age')
