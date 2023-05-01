from django.contrib import messages
from django.core.mail.message import EmailMessage

ERROR_MESSAGE = "Sorry, we were unable to process that! Please make sure all" \
                " your information is entered correctly."


def handle_validation_error(request):
    """
    Creates an error message to display in the browser when an error occurs on
    form submission
    :param request: the HTTP request for sending the form data
    """
    messages.error(request, ERROR_MESSAGE)


def send_email(subject, message, to_email):
    """
    Composes and sends an email
    :param subject: the email subject
    :param message: the email message body
    :param to_email: the address to which to send the email
    """
    email_message = EmailMessage(subject=subject,
                                 body=message,
                                 to=[to_email])
    email_message.send()
