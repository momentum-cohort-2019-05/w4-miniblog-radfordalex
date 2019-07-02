import datetime
from django import forms
from django.db.models import TextField
from .models import BlogPost, Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('user', 'target_blog_post', 'comment',)