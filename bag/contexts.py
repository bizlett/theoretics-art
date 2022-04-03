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

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            art = Art.objects.all()
            photography = Photography.objects.all()

            if product.category.name == "art":
                for art_piece in art:
                    total += item_data * art_piece.price

            elif product.category.name == "photography":
                for art_piece in photography:
                    total += item_data * art_piece.price

            product_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
                'art': art,
                'photography': photography,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            photography.objects.all()
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * photography.price
                product_count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'photography': photography,
                    'size': size,
                })
    
    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
