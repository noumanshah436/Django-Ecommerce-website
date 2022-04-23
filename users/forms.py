from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class CustomUserForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': ' form-control  my-2', 'placeholder': 'Enter Username'}))
    email = forms.CharField(
        widget=forms.TextInput(attrs={'class': ' form-control  my-2', 'placeholder': 'Enter Email'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': ' form-control  my-2', 'placeholder': 'Enter Password'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': ' form-control  my-2', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    # email = forms.EmailField()
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': ' form-control  my-2'}))
    email = forms.CharField(
        widget=forms.TextInput(attrs={'class': ' form-control  my-2'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    image = forms.FileField(
        widget=forms.FileInput(attrs={'class': 'rounded_list my-2'}))
    phone = forms.CharField(
        widget=forms.TextInput(attrs={'class': ' form-control  my-2'}))
    address = forms.CharField(
        widget=forms.Textarea(attrs={'class': ' form-control  my-2'}))

    class Meta:
        model = Profile
        fields = ['image', 'phone', 'address']
