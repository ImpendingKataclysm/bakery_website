from django.shortcuts import render


def home(request):
    """
    :param request: HTTP request to render specified content
    :return: HTTP response containing request result
    """
    return render(request, "index.html")
