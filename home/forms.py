from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from home.models import *

class RegisterForm(forms.ModelForm):
    username = forms.CharField(label='username',max_length=100,required=True)
    email = forms.EmailField(label='email',required=True)
    first_name = forms.CharField(label='first_name',max_length=100,required=True)
    password = forms.CharField(label='password1',required=True,max_length=100)
    password2 = forms.CharField(label='password2',required=True,max_length=100)

    class Meta:
        model = User
        fields =['username','email','first_name','password',]

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")
        if password1 and password2 and password2!=password1:
            raise forms.ValidationError("Password and Confirm Password Mismatched!!")

class LoginForm(forms.Form):
    username = forms.CharField(label='username',max_length=100)
    password = forms.CharField(label='password',max_length=100)

    def clean(self):
        cleaned_data = super().clean()

        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        user = authenticate(username=username,password=password)
        if user is None:
            raise forms.ValidationError('UnAuthenticated User')
        
class UserUpdationForm(forms.ModelForm):
    first_name = forms.CharField(label='first_name',required=True,max_length=100)
    second_name = forms.CharField(label='second_name',required=True,max_length=100)
    email = forms.EmailField(label='email',required=True)
    phone = forms.IntegerField(required=True)
    # age = forms.IntegerField(required=True)
    address = forms.CharField(max_length=300)

    class Meta:
        model = UserProfile
        fields =['first_name','second_name','email','phone','address']
