from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

from .models import Complain

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    mobile = forms.IntegerField(required=True, help_text='Mobile is required.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2','mobile')

class LoginForm(forms.Form):
    username = forms.CharField(required=True, help_text="Username is required!")
    password = forms.CharField(widget=forms.PasswordInput, required=True, help_text="Password is required!")


class ComplainForm(forms.ModelForm):
    class Meta:
        model = Complain
        fields = ('title','description','location')