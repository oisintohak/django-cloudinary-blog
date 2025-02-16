from .models import Comment, Post
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title', 'author', 'slug', 'featured_image', 'image', 'content',
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
