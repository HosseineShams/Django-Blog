from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    bio = forms.CharField(label="bio", required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', label_suffix="", widget=forms.TextInput(attrs={'class': "input100", "title": ""}))
    password = forms.CharField(label='Password', label_suffix="", widget=forms.PasswordInput(attrs={'class': "input100", "title": ""}))


class ProfileForm(forms.ModelForm):
    bio = forms.CharField(label="bio", required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {
            "username":'Username',
            "first_name":'First Name',
        }

        help_texts = {
            "username": ""
        }


    def clean_username(self):
        cleaned_data = self.clean()
        username = cleaned_data['username']
        if len(username) < 5:
            self.add_error('username', 'Username must be at least 5 characters')
        return username
        