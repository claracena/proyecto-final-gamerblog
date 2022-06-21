from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nombre'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'message': forms.Textarea(attrs={'placeholder': 'Escriba su mensaje...'}),
            'type': forms.Select(attrs={'style': 'width: -webkit-fill-available !important;'}),
        }

