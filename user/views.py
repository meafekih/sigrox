from django.http import HttpResponse
from django.template import loader
from .models import user

def sayHello(request):
    tmp = loader.get_template('user.html')
    data = user.objects.all()
    context={
        'users' : data
    }
    return HttpResponse(tmp.render(context, request))

# Create your views here.
