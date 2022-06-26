from django import forms
from .models import Contact

""" class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nombre'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'message': forms.Textarea(attrs={'placeholder': 'Escriba su mensaje...'}),
            'type': forms.Select(attrs={'style': 'width: -webkit-fill-available !important;'}),
        }

"""

class ContactForm(forms.ModelForm):
    
    name =  forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}))
    last_name =  forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}))
    email =  forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    message =  forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Mensaje'}))

    class Meta:
        model = Contact
        fields = '__all__'