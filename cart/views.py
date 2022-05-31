from django.shortcuts import render, redirect, get_object_or_404
from clothing.models import Category, Items
from django.views.decorators.http import require_POST
from .cart import Cart
from .forms import CartAddProductForm
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_http_methods



@require_POST
def cart_add(request, id):
    item = Items.objects.get(id=id)

    if request.session['item']:
        x = request.session['total']
        request.session['total'] = float(item.price) + float(total)
        
    else:
        request.session['item_id'] = id
        request.session['item_id']['name'] = item.name
        request.session['total'] = item.price
        
    total = request.session['total']

    session.modified = True
    return render(request, 'shoes_page.html',{'total':total})

@require_http_methods(['POST'])
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Item, id=product_id)
    cart.remove(product)
    return redirect('shoes_page.html')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/cart_detail.html',{'cart':cart})


