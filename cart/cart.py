from decimal import Decimal
from django.conf import settings
from clothing.models import Items, Category

class Cart(object):

    def add(self, product, quantity=1, override_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity':0,
                                     'price' : str(product.price)}
        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def remove(self,product, category):
        product_id=str(product.id)
        if product_id in self.cart:
            del self.cart[product_id,category]
            self.save()

    def save(self):
        self.session.modified=True

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[setting.CART_SESSION_ID]
        self.save()

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Items.objects.filter(id__in=product_id)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        
        for item in cart.values():
            item['prices'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart