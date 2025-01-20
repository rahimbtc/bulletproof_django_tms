from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.utils.html import format_html

from .models import UserModel
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    """
    Custom admin for the CustomUser model.
    """

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = UserModel

    # Fields to display in the admin list view
    list_display = ("username", "email", "phone_number", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active", "groups")
    readonly_fields = ("last_login", "date_joined")

    # Fields to display in the admin detail/edit view
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal Info", {"fields": ("email", "phone_number")}),
        (
            "Permissions",
            {"fields": ("is_staff", "is_active", "groups", "user_permissions")},
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    # Fields to display in the admin add view
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "phone_number",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )

    # Fields to search in the admin list view
    search_fields = ("username", "email", "phone_number")
    ordering = ("username",)


# Register the CustomUser with the customized admin
admin.site.register(UserModel, CustomUserAdmin)
