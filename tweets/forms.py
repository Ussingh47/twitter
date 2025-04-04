from django import forms
from .models import Tweet, Comment

class TweetForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 3, 
            'placeholder': "What's happening?",
            'class': 'form-control'
        }),
        max_length=280
    )
    image = forms.ImageField(required=False)
    
    class Meta:
        model = Tweet
        fields = ['content', 'image']

class CommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 2, 
            'placeholder': "Add a comment...",
            'class': 'form-control'
        }),
        max_length=280
    )
    
    class Meta:
        model = Comment
        fields = ['content']
