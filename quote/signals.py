from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Application
from .models import QuoteRequest

@receiver(post_save, sender=QuoteRequest)
def send_email_notification(sender, instance, created, **kwargs):
    if created:
        send_mail(
            "Новая заявка на сайте",
            f"Имя: {instance.name}\nEmail: {instance.email}\nСообщение: {instance.details}",
            "your_email@gmail.com",  # Отправитель
            ["your_email@gmail.com"],  # Получатель
            fail_silently=False,
        )
