from django.contrib import admin
from .models import Photo

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'address', 'image_preview')
    search_fields = ('title', 'address')
    
    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="100" height="auto"/>'
        return "No Image"
    
    image_preview.allow_tags = True
    image_preview.short_description = "Preview"


