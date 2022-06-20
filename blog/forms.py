from django import forms
from .models import Blog

class PostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'