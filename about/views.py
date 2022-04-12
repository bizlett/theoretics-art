from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def about(request):
    """ A view to return the about page """

    template = 'about/about.html'
    return render(request, template)
