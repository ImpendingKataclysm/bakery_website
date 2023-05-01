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


class ApplicationForm(forms.Form):
    """
    Collects the information entered by the user into the job application form
    """
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    start_date = forms.DateField()
    employment_status = forms.CharField()
    resume = forms.FileField()
