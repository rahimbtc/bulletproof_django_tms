from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserModel


class CustomUserCreationForm(UserCreationForm):
    """
    Custom form for creating new users. Includes all required fields
    and a repeated password field.
    """

    class Meta:
        model = UserModel
        fields = ("username", "email", "phone_number")  # Include the fields you want to expose


class CustomUserChangeForm(UserChangeForm):
    """
    Custom form for updating existing users.
    """

    class Meta:
        model = UserModel
        fields = (
            "username",
            "email",
            "phone_number",
        )  # Include fields you want to allow updates on
