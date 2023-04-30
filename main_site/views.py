from django.shortcuts import render
from django.core.mail.message import EmailMessage
from django.conf import settings
from django.contrib import messages
from datetime import datetime

from .forms import SendEmailForm
from .models import Email
from .functions import handle_validation_error


def home(request):
    """
    :param request: HTTP request to render the home page
    :return: HTTP response used to render the home page in the browser
    """
    return render(request, "index.html")


def about(request):
    """
    :param request: HTTP request to render the about page
    :return: HTTP response used to render the about page in the browser
    """
    return render(request, "about.html")


def contact(request):
    """
    :param request: HTTP request to render the contact page
    :return: HTTP response used to render the contact page in the browser
    """
    if request.method == 'POST':
        form = SendEmailForm(request.POST)

        if form.is_valid():
            sender_name = form.cleaned_data["sender_name"]
            sender_email = form.cleaned_data["sender_email"]
            message = form.cleaned_data["message"]

            Email.objects.create(sender_name=sender_name,
                                 sender_email=sender_email,
                                 date_sent=datetime.now(),
                                 message=message)

            # Confirmation email not implemented at this time
            # No app password configured
            email_subject = f"Message received from {sender_name} ({sender_email})"
            email_message = EmailMessage(subject=email_subject,
                                         body=message,
                                         to=[settings.EMAIL_HOST_USER])
            # email_message.send()

            success_message = f"Thanks for reaching out, {sender_name.title()}!"
            messages.success(request, success_message)
        else:
            handle_validation_error(request)

    return render(request, "contact.html")
