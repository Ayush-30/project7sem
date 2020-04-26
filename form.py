from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class createuserform(UserCreationForm):
    email = forms.EmailField(required=True,
                             label='Email',
                             error_messages={'exists': 'Oops'})
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


