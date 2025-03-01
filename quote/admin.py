from django.contrib import admin
from .models import QuoteRequest

class QuoteRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'details', 'created_at')
    list_filter = ('name', 'email', 'details', 'created_at')

admin.site.register(QuoteRequest, QuoteRequestAdmin)
