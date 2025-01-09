from django import forms
from . import models
from .models import Comment

class CreatePost(forms.ModelForm):   
    class Meta:
        model = models.Post
        fields = ('title','body','platform','playstyle','slug')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment 
        fields = ('name', 'body')