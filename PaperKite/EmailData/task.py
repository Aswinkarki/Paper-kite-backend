from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_subscription_email(email):
    subject = "Thank You for Subscribing to PaperKite"
    message = "We appreciate your support. Stay tuned for exciting updates!"
    
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,  # Uses the email from settings.py
        [email],
        fail_silently=False,
    )
    
    return f"Email sent to {email}"
