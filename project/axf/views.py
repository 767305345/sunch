from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'axf/home.html')

def mine(request):
    return render(request,'axf/mine.html')

def cart(request):
    return render(request,'axf/cart.html')

def market(request):
    return render(request,'axf/market.html')

def base(request):
    return render(request,'axf/base.html')
