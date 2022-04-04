from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product, Art, Photography


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        art = Art.objects.all()
        photography = Photography.objects.all()

        if product.category.name == "art":
            for art_piece in art:
                if art_piece.name == product.name:
                    total += quantity * art_piece.price
        else:
            if product.category.name == "photography":
                for art_piece in photography:
                    if art_piece.name == product.name:
                        total += quantity * art_piece.price
        
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })
    
    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
        'art': art,
        'photography': photography,
    }

    return context
