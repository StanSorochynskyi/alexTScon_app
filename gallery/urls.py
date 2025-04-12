from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import all_content_view

urlpatterns = [
    path('', all_content_view, name='all_content'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
