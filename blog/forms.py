from django import forms
from .models import Tag, Platform, Blog

class ArticleForm(forms.ModelForm):

    image = forms.FileField(label='Imágen')
    title = forms.CharField(label='Título', widget=forms.TextInput(attrs={'class': 'form-control'}))
    body = forms.CharField(label='Artículo', widget=forms.Textarea(attrs={'class': 'form-control'}))
    tags = forms.ModelMultipleChoiceField(label='Etiquetas', queryset=Tag.objects.all().distinct(), widget=forms.CheckboxSelectMultiple())
    platforms = forms.ModelMultipleChoiceField(label='Plataformas', queryset=Platform.objects.all().distinct(), widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Blog
        fields = ('image', 'title', 'body', 'tags', 'platforms')

        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'form-control'}),
        #     'body': forms.Textarea(attrs={'class': 'form-control'}),
        #     'tags': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
        #     'platforms': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
        # }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['image'].label = 'Imagen de portada'
    #     self.fields['title'].label = 'Titulo'
    #     self.fields['body'].label = 'Articulo'
    #     self.fields['tags'].label = 'Etiquetas'
    #     self.fields['platforms'].label = 'Plataformas'
    #     self.fields['title'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['body'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['tags'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['platforms'].widget.attrs.update({'class': 'form-control'})

    # class Meta:
    #     model = Blog
    #     fields = ('image', 'title', 'body', 'tags', 'platforms')