from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'subtitle', 'body', 'image']


class BlogSearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, label='Buscar')
