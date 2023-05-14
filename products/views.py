from django.http import HttpResponse
from django.template import loader
from .models import products

def all_products(request):
    temp  = loader.get_template('products.html')
    data = products.objects.all().order_by('-price').values()
    #data = products.objects.filter(price<1000)
    #data = products.objects.values_list('name', 'price')
    #data = products.objects.filter('price'<1000)
    context ={'all_products':data,}
    return HttpResponse(temp.render(context, request))

def details(request, id):
    temp = loader.get_template('product.html')
    data = products.objects.get(id=id)
    context={'product':data}
    return HttpResponse(temp.render(context, request))

def main(request):
    data = [
        {'name':'amine', 'version': 4},
        {'name':'barbara', 'version': 3},
        {'name':'kongo', 'version': 4},
        {'name':'pikatchu', 'version': 5},
    ]
    context={'data':data}
    temp = loader.get_template('main.html')
    return HttpResponse(temp.render(context, request))


    
