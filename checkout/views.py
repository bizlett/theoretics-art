from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Ke1HwBBfN1uxc5WbEehmorYlpZybgdn6IG7rvSZE9sYy5rsBd4s22c6tu1cGLud55ZIqhgzVszc0i6Jvx9kIdfk00v50UGhY3',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)