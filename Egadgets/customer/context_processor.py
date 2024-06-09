from account.models import Cart,Orders

def cart_count(request):
    if request.user.is_authenticated:
        count=Cart.objects.filter(user=request.user).count()
        return{"count":count}
    else:
        return{"count":0}

def order_count(request):
    if request.user.is_authenticated:
        count=Orders.objects.filter(user=request.user).count()
        return{"orderr":count}
    else:
        return{"orderr":0}


