from django import forms
from custom_user import models


class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = models.MyUser
        fields = ['displayname']