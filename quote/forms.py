from django import forms
from .models import QuoteRequest

class QuoteRequestForm(forms.ModelForm):
    class Meta:
        model = QuoteRequest
        fields = ['contact_name', 'company_name', 'address', 'website', 'email', 'phone_number', 'quote_number', 'date', 'description']