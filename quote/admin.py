from django.contrib import admin
from .models import QuoteRequest

class QuoteRequestAdmin(admin.ModelAdmin):
    list_display = ('contact_name', 'company_name', 'address',
                    'website', 'email', 'phone_number',
                    'quote_number', 'date', 'description')
    list_filter = ('contact_name', 'company_name', 'address',
                    'website', 'email', 'phone_number',
                    'quote_number', 'date', 'description')

admin.site.register(QuoteRequest, QuoteRequestAdmin)
