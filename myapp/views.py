from django.shortcuts import render, HttpResponse
from django.template import loader


# Create your views here.

def index2(request):
    return HttpResponse("Hello Yin, this is your first Django. ")

def index(request):
    template = loader.get_template('myapp/index.html')
    context = {
        'test context': 111111
    }
    return HttpResponse(template.render(context, request))


def getdata(request):
    name = request.POST['username']
    pwd = request.POST['password']
    print('name = '+name)
    print('pwd = '+pwd)   
    return 'here is the data' 
