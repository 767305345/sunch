from django.shortcuts import render
from .models import Whell

# Create your views here.
def home(request):
    whellsList=Whell.objects.all()
    return render(request,'axf/home.html',{"title":'主页'
                                                   ,''"whellsList":whellsList})

def mine(request):
    return render(request,'axf/mine.html',{"title":'我的'})

def cart(request):
    return render(request,'axf/cart.html',{"title":'购物车'})

def market(request):
    return render(request,'axf/market.html',{"title":'商场'})

def base(request):
    return render(request,'axf/base.html',{"title":'主页'})
