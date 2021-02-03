from sixth_app.models import UserModel
from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields=('username','email','password')

class UserProfile(forms.ModelForm):
    class Meta():
        model = UserModel
        fields=('profile_pic','website_link')

