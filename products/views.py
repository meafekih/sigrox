from django.http import HttpResponse
from django.template import loader
from .models import products


def all_products(request):
    temp  = loader.get_template('products.html')
    data = products.objects.all()
    context ={'all_products':data,}
    return HttpResponse(temp.render(context, request))

def details(request, id):
    temp = loader.get_template('product.html')
    data = products.objects.get(id=id)
    context={'product':data}
    return HttpResponse(temp.render(context, request))



    
