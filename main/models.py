from django.conf import settings
from django.core.mail import send_mail
from django.db import models


class Email(models.Model):
    REPLY_TITLE = "A notification from Company"
    REPLY_MSG = "Hello, {}!\n\nThank you for contacting.\nWe'll response to your email.\n\nKind regards, Company"

    created_timestamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    reply_email = models.EmailField()
    sender_ip = models.GenericIPAddressField()
    sender_name = models.CharField(max_length=100)

    def email_send(self):
        """Send a default template email to a client and his question to the main inbox"""

        title = f"Site message from: {self.sender_name}"
        timestamp = self.created_timestamp.strftime("%b %d, %Y %H:%M:%S")
        message = f"{self.message}\n\nEmail for reply: {self.reply_email}\n\nCreation date of message: {timestamp}"
        send_mail(
            subject=title,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
        )
        send_mail(
            subject=self.REPLY_TITLE,
            message=self.REPLY_MSG.format(self.sender_name),
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.reply_email],
        )


class Press(models.Model):
    author = models.CharField(max_length=100)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    text = models.TextField()
    source = models.URLField()

    class Meta:
        verbose_name_plural = "Press"

    def __str__(self):
        return self.title
