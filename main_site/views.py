from django.shortcuts import render


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
