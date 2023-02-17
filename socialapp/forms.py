from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from socialapp.models import Posts,Userprofile





class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","last_name","username","email","password1","password2"]

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

class PostForm(forms.ModelForm):
    class Meta:
        model=Posts
        fields=[
            "post",
            "image"

        ]
        widgets={
            "post":forms.Textarea(attrs={"class":"form-control","row":1}),
            "image":forms.FileInput(attrs={"class":"form-select"}),
        }


class UserdetailForm(forms.ModelForm):
    class Meta:
        model=Userprofile
        fields=[
            "place",'dob','phone',"image"
        ]


        widgets={
            "place":forms.TextInput(attrs={"class":"form-control"}),
            "dob":forms.TextInput(attrs={"class":"form-control"}), 
            "phone":forms.NumberInput(attrs={"class":"form-control"}),
            "image":forms.FileInput(attrs={"class":"form-select"}),
        }