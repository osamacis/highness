from django import forms
from .models import ContactInquiry

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactInquiry
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control rounded-pill px-3 py-2',
                'placeholder': 'Your Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control rounded-pill px-3 py-2',
                'placeholder': 'Your Email'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control rounded-pill px-3 py-2',
                'placeholder': 'Phone Number (Optional)'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control rounded-pill px-3 py-2',
                'placeholder': 'Subject'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control rounded-4 px-3 py-2',
                'placeholder': 'Your Message',
                'rows': 5
            }),
        }
