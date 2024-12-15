from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100,required=True)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=100,required=True)
    password1 = forms.CharField(required=True,max_length=100)
    password2 = forms.CharField(required=True,max_length=100)
