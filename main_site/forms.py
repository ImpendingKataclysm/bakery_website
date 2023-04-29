from datetime import datetime
from django import forms


class SendEmailForm(forms.Form):
    """
    Collects the information entered by the user into the email form
    """
    sender_name = forms.CharField()
    sender_email = forms.EmailField()
    date_sent = datetime.now()
    message = forms.CharField(widget=forms.Textarea)
