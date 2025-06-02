from django import forms
from .models import Contact  # ou le modèle que tu utilises

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact  # remplace par ton modèle
        fields = ['first_name', 'last_name', 'email', 'subject', 'message']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'input-field', 
                'placeholder': 'First Name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'input-field', 
                'placeholder': 'Last Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'input-field', 
                'placeholder': 'Email'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'input-field', 
                'placeholder': 'Subject'
            }),
            'message': forms.Textarea(attrs={
                'class': 'textarea-field', 
                'placeholder': 'Votre message ici...', 
                'rows': 5
            }),
        }
