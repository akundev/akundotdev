from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "username"]

    fieldsets = (
        *UserAdmin.fieldsets,  # original form fieldsets, expanded
        (  # new fieldset added on to the bottom
            "Profile Image",  # group heading of your choice; set to None for a blank space instead of a header
            {
                "fields": (
                    "photo",
                    "github_link",
                    "linkedin_link",
                    "cv_link",
                    "public_email",
                    "main_user",
                )
            },
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)
