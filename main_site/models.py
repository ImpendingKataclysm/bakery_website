from django.db import models

MAX_FIELD_LEN = 80


class Email(models.Model):
    """
    Emails received from the public
    """
    sender_name = models.CharField(max_length=MAX_FIELD_LEN)
    sender_email = models.EmailField()
    date_sent = models.DateTimeField()
    message = models.TextField()

    def __str__(self):
        return f"From {self.sender_name} ({self.sender_email}) on {self.date_sent}: {self.message}"


class JobApplicant(models.Model):
    """
    Job applications received online
    """
    first_name = models.CharField(max_length=MAX_FIELD_LEN)
    last_name = models.CharField(max_length=MAX_FIELD_LEN)
    email = models.EmailField(null=True)
    date_applied = models.DateTimeField()
    date_available = models.DateTimeField()
    employment_status = models.CharField(max_length=MAX_FIELD_LEN)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"
