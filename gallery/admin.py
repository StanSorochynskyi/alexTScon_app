from django.contrib import admin
from .models import Promo, Photo, Advertize, Annonsment, Contact

@admin.register(Promo)
class PromoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'link')
    search_fields = ('title', 'description', 'link')

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('image_preview', 'title', 'address')
    search_fields = ('title', 'address')
    
    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="100" height="auto"/>'
        return "No Image"
    
    image_preview.allow_tags = True
    image_preview.short_description = "Preview"


@admin.register(Advertize)
class AdvertizeAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'link')
    search_fields = ('title', 'description', 'image', 'link')

@admin.register(Annonsment)
class AnnonsmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'link')
    search_fields = ('title', 'description', 'link')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'link')
    search_fields = ('title', 'description', 'link')