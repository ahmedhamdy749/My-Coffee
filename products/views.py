from django.shortcuts import render,get_object_or_404
from datetime import datetime
from .models import Product

# Create your views here.
def products(requset):
    pro = Product.objects.all()
    name = None
    desc = None
    pfrom = None
    pto = None
    cs = None

    if 'cs' in requset.GET:
        cs = requset.GET['cs']
        if not cs:
            cs = 'off'


    if 'searchname' in requset.GET:
        name = requset.GET['searchname']
        if name:
            if cs =='on':
                pro = pro.filter(name__contains = name)
            else:
                pro = pro.filter(name__icontains = name)
            


    if 'searchdesc' in requset.GET:
        desc = requset.GET['searchdesc'] 
        if desc:
            if cs=='on':
                pro=pro.filter(description__contains = desc)
            else:
                pro=pro.filter(description__icontains = desc)    
             

    if 'searchpricefrom' in requset.GET and 'searchpriceto' in requset.GET:
        pfrom = requset.GET['searchpricefrom']
        pto = requset.GET['searchpriceto']
        if pfrom and pto:
            if pfrom.isdigit() and pto.isdigit():
                pro = pro.filter( price__gte = pfrom, price__lte = pto )


    context = {
        'products':pro,
        
    }
    return render(requset,'products/products.html',context)
def product(requset ,pro_id):
    context = {
        'pro':get_object_or_404(Product,pk=pro_id)
    }
    return render(requset,'products/product.html',context)
def search(requset):
    return render(requset,'products/search.html')
