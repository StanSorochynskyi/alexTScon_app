from django.contrib import admin
from .models import Project, Photo

class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1  # Allows adding photos inline in the admin

class ProjectAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]

admin.site.register(Project, ProjectAdmin)
