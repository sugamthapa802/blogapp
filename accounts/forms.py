from django import forms
from .models import CustomUser,Profile,Follow
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.forms import AuthenticationForm

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


class CrispyAuthenticationForm(AuthenticationForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper=FormHelper()
        self.helper.form_method='POST'
        self.helper.add_input(Submit('login','login'))