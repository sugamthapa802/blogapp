from django.contrib import admin
from .models import CustomUser,Profile,Follow
from .forms import CustomUserChangeForm,CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    form=CustomUserChangeForm
    add_form=CustomUserCreationForm
    list_display=('email','username','is_staff','is_active',)
    list_filter=('email','username','is_staff','is_active',)
    fieldsets=(
        ("Customise User's Info",{'fields':('email','username','password',)}),
        ('Permissions',{'fields':('is_staff','is_active','groups','user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(Profile)
admin.site.register(Follow)
