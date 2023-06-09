from django import forms

from .models import Post

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ( "username", "email" )

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
