from django.shortcuts import render, redirect
from .models import TweetModel, Product
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    user = request.user.is_authenticated
    if user:
        return redirect('/erp')
    else:
        return redirect('/sign-in')


def erp(request):
    return render(request, 'erp/home.html')


@login_required
def product_list(request):
    if request.method == 'GET':
        user = request.user_is_authenticated
        if user:
            all_products = Product.objects.all().order_by('-amount')
            return render(request, 'erp/home.html', {'product': all_products})
        else:
            return redirect('sign-in')
    elif request.method == 'POST':
        selected_value = request.POST.get('cloth')
        return redirect(request, '/erp', {'selected_value': selected_value})
    # 등록 된 상품의 리스트를 볼 수 있는 view


@login_required
def product_inbound(request):
    my_product = request.objects.get(code=code)



@login_required
def product_outbound(request):
    product_code = Product.objects.get(code=code)



@login_required
def product_create(request):

    return request
    # 상품 등록 view

