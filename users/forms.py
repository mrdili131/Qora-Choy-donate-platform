from django import forms
from .models import User

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

class RegisterForm(forms.Form):
    username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    number = forms.CharField()
    checkmark = forms.BooleanField(required=True)
    password = forms.CharField(widget=forms.PasswordInput())
    password1 = forms.CharField(widget=forms.PasswordInput())

    def validate(self):
        if self.password == self.password1:
            return self.password