from django import forms
from .models import Tag, Platform, Blog, Comment

class ArticleForm(forms.ModelForm):

    image = forms.FileField(label='Imágen')
    title = forms.CharField(label='Título', widget=forms.TextInput(attrs={'class': 'form-control'}))
    body = forms.CharField(label='Artículo', widget=forms.Textarea(attrs={'class': 'form-control'}))
    tags = forms.ModelMultipleChoiceField(label='Etiquetas', queryset=Tag.objects.all().distinct(), widget=forms.CheckboxSelectMultiple())
    platforms = forms.ModelMultipleChoiceField(label='Plataformas', queryset=Platform.objects.all().distinct(), widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Blog
        fields = ('image', 'title', 'body', 'tags', 'platforms')

class CommentForm(forms.ModelForm):

    # email = forms.CharField(
    #     label='',
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'form-control',
    #             'placeholder': 'E-mail',
    #             'value': 'asd@asd.com'
    #         }
    #     )
    # )
    # name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre', 'value': 'asd'}))
    # website = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sitio Web', 'value': 'asd.com'}))
    message = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Comentario', 'value': 'asd asd asd asd asd dasd'}))

    class Meta:
        model = Comment
        fields = ('message',)
