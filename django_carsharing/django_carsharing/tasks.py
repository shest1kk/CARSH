from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_email_task():
    subject = 'Test Email'
    message = 'This is a test email sent to MailHog.'
    from_email = 'from@example.com'
    recipient_list = ['to@example.com']

    send_mail(subject, message, from_email, recipient_list, fail_silently=False)
