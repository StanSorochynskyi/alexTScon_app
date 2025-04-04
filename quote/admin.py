from django.contrib import admin
from .models import QuoteRequest

class QuoteRequestAdmin(admin.ModelAdmin):
    list_display = ('contact_name', 'address', 'email', 'phone_number', 'description', 'date')
    list_filter = ('contact_name', 'address', 'email', 'phone_number', 'description', 'date')

admin.site.register(QuoteRequest, QuoteRequestAdmin)
