from django.shortcuts import render,get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse



def cart_summary(request):
    cart=Cart(request)
    return render(request,'cart/cart-summary.html',{'cart':cart})

def cart_add(request):
    cart=Cart(request)
    if request.POST.get('action')=='post':
        product_id=int(request.POST.get('product_id'))
        product_quantity=int(request.POST.get('product_quantity'))
        product=get_object_or_404(Product,id=product_id)
        cart.add(product=product,product_qty=product_quantity)
        cart_quantity=cart.__len__()
        
        reponse =JsonResponse({'qty':cart_quantity})
        
        return reponse
        

def cart_delete(request):
    cart=Cart(request)
    if request.POST.get('action')=='post':
        product_id=int(request.POST.get('product_id'))
        cart.delete(product=product_id)
        cart_quantity=cart.__len__()
        cart_total=cart.get_total()
        reponse=JsonResponse({'qty':cart_quantity,'total':cart_total})
        return reponse
def cart_update(request):
    pass




