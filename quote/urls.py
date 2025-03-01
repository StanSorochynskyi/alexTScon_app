from django.urls import path
from .views import RequestQuoteView

urlpatterns = [
    path("", RequestQuoteView.as_view(), name="quote"),
]