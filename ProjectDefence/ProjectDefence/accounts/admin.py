from ProjectDefence.accounts.forms import ProfileFullfilForm
from ProjectDefence.accounts.models import Profile
from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model

# Register your models here.

UserModel = get_user_model()


@admin.register(UserModel)
class AppUserAdmin(auth_admin.UserAdmin):
    ordering = ('email',)
    list_display = ['pk', 'email', 'last_login', 'profile']
    list_filter = ()
    fieldsets = (
        (None, {"fields": ("password",)}),
        ("Personal info", {"fields": ("email",)}),
        (
            "Permissions",
            {
                "fields": (

                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Important dates", {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2",),
            },
        ),
    )


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    ordering = ('pk', 'first_name', 'last_name')
    list_display = ['user', 'first_name', 'last_name', 'city', 'number', 'street', 'image', ]
    add_form = ProfileFullfilForm
    list_filter = ('city', 'street')
    search_fields = ('first_name', 'last_name', 'user__email', 'number', 'city', 'street',)
    sortable_by = ('user', 'first_name', 'last_name', 'number',)
