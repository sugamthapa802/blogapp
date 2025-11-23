from django import forms
from .models import CustomUser,Profile,Follow
from django.contrib.auth.forms import UserCreationForm,UserChangeForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields=('email','username',)
    def save(self, commit=True):
        user = super().save(commit=False)
        # custom logic here
        if commit:
            user.save()
        return user  # <-- critical

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model=CustomUser
        fields=('email','username',)