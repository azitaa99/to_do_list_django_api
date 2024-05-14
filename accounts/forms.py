
from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RegisterForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),required=True)
    re_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),required=True)
    

    def clean_username(self):
        username=self.cleaned_data['username']
        user=User.objects.filter(username=username).exists()
        if user:
            raise ValidationError('this username already exist! try another one')
        return username

    def clean_email(self):
        email=self.cleaned_data['email']
        user=User.objects.filter(email=email).exists()
        if user:
          raise ValidationError('email already exists')
        return email
    
    def clean(self):
        cd= super().clean()
        pass1=cd.get('password')
        pass2=cd.get('re_password')
        if pass1 and pass2 and pass1 != pass2 :
            raise ValidationError('passwords not same!')
        
        
        
      
class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),required=True)
    