from django.db import models

MAX_FIELD_LEN = 80


class Email(models.Model):
    """
    Database table for emails received from the public
    """
    sender_name = models.CharField(max_length=MAX_FIELD_LEN)
    sender_email = models.EmailField()
    date_sent = models.DateTimeField()
    message = models.TextField()

    def __str__(self):
        return f"From {self.sender_name} ({self.sender_email}) on {self.date_sent}: {self.message}"
