from django import forms
from .models import QuoteRequest

class QuoteRequestForm(forms.ModelForm):
    class Meta:
        model = QuoteRequest
        fields = ['contact_name', 'address', 'email', 'phone_number', 'description', 'date']