from django.shortcuts import render
from django.core.mail.message import EmailMessage
from django.conf import settings
from django.contrib import messages
from datetime import datetime

from .forms import SendEmailForm, ApplicationForm
from .models import Email, JobApplicant
from .functions import handle_validation_error


def home(request):
    """
    :param request: HTTP request to render the home page
    :return: HTTP response used to render the home page in the browser
    """
    return render(request, "index.html")


def about(request):
    """
    Displays the about page
    :param request: HTTP request to render the about page
    :return: HTTP response used to render the about page in the browser
    """
    return render(request, "about.html")


def contact(request):
    """
    Displays the contact page and collects the data entered by the user into the contact form
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


def products(request):
    """
    Displays the product page
    :param request: HTTP request
    :return:HTTP response
    """
    return render(request, "products.html")


def jobs(request):
    """
    Displays the job application page and accepts user applications and resume uploads
    :param request: HTTP request
    :return: HTTP response
    """
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)

        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            date_applied = datetime.now()
            date_available = form.cleaned_data["start_date"]
            employment_status = form.cleaned_data["employment_status"]
            resume = request.FILES['resume']

            JobApplicant.objects.create(first_name=first_name,
                                        last_name=last_name,
                                        email=email,
                                        date_applied=date_applied,
                                        date_available=date_available,
                                        employment_status=employment_status)
        else:
            print(form.errors)

    return render(request, "jobs.html")
