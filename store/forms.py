from django import forms
from django.contrib.auth.models import User
from .models import Product
from django.forms import ModelForm


# from django.contrib.auth.forms import UserCreationForm
#
#
# class CustomUserForm(UserCreationForm):
#     username = forms.CharField(
#         widget=forms.TextInput(attrs={'class': ' form-control  my-2', 'placeholder': 'Enter Username'}))
#     email = forms.CharField(
#         widget=forms.TextInput(attrs={'class': ' form-control  my-2', 'placeholder': 'Enter Email'}))
#     password1 = forms.CharField(
#         widget=forms.PasswordInput(attrs={'class': ' form-control  my-2', 'placeholder': 'Enter Password'}))
#     password2 = forms.CharField(
#         widget=forms.PasswordInput(attrs={'class': ' form-control  my-2', 'placeholder': 'Confirm Password'}))
#
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']


class ProductForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'mb-3 '

    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['seller']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control  mb-3'}),
            'slug': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'description': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'product_image': forms.FileInput(attrs={'class': 'form-control  mb-3'})
        }
