

from django import forms
from .models import Post


class NoteForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'url', 'description']
