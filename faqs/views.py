from django.shortcuts import render


def faqs(request):
    """ A view to return the faqs page """

    template = 'faqs/faqs.html'
    return render(request, template)
