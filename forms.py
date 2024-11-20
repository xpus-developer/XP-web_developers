from django import forms
from .models import ContactMessage  # Import the model

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'phone', 'email', 'message']

