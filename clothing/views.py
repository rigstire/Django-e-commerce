from django.shortcuts import render
from .models import Items, Category
from decimal import Decimal
from django.views.decorators.http import require_http_methods

def home(request):
    return render(request,'home.html')

def clothing(request):
    clothing = Items.objects.filter(category__category='Clothing')
    return render(request, 'clothing/clothing_page.html',{'clothing':clothing})

def shoes(request):
    shoes = Items.objects.filter(category__category='Shoes')  

    return render(request, 'shoes/shoes_page.html',{'shoes':shoes,
                                                    
                                                    })

def accessories(request):
    accessories = Items.objects.filter(category__category='Accessories')
    return render(request, 'accessories/accessories_page.html', {'accessories':accessories})


def add_item(request,id):
    product = Items.objects.get(id=id)


    if 'product' in request.session:
        total = product.price + Decimal(request.session['total'])
        request.session['total'] = str(total)

        products = request.session['product']
        products.append(id)
        request.session['product'] = products
        temp = int(request.session['total_items'])
        temp+1
        request.session['total_items'] = str(temp)

    else:
        request.session['product'] = [id]
        request.session['total'] = str(product.price)
        request.session['total_items'] = 1

    request.session.modified = True
    return render(request, 'base.html',{'product':request.session['product'], 
                                        'total':request.session['total'],
                                        'total_items':request.session['total_items']})

def delete_item(request, id):
    product = Items.objects.get(id=id)
    product_list = request.session['product']
    product_list.remove(id)
    total = Decimal(request.session['total'])
    total = total-Decimal(product.price)
    total_items = int(request.session['total_items']) - 1


    request.session['total_items'] = str(total_items)
    request.session['total'] = str(total)
    request.session['product'] = product_list
    request.session.modified = True



    return render(request, 'cart/cart_detail.html')




def cart_detail(request):
    
    if 'product' in request.session:
        products = Items.objects.filter(pk__in=request.session['product'])
        total = request.session['total']
        total_items = request.session['total_items']

    else:
        products = None
        total = None
        total_items = 0

    return render(request, 'cart/cart_detail.html', {'products':products,'total':total, 'total_items':total_items,},)