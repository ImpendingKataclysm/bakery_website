from django.contrib import messages

ERROR_MESSAGE = "Sorry, we were unable to process that! Please make sure all" \
                " your information is entered correctly."


def handle_validation_error(request):
    """
    Creates an error message to display in the browser when an error occurs on
    form submission
    :param request: the HTTP request for sending the form data
    """
    messages.error(request, ERROR_MESSAGE)
