from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Question

# Create your views here.

def index2(request):
    return HttpResponse("Hello Yin, this is your first Django. ")

def index3(request):
    template = loader.get_template('myapp/index.html')
    context = {
        'test context': 111111
    }
    return HttpResponse(template.render(context, request))

def index(request):
    latest_question_list = Question.objects.order_by('pub_date')[:5]
    output = ', '.join([p.question_text for p in latest_question_list])
    return HttpResponse(output)


def getdata(request):
    name = request.POST['username']
    pwd = request.POST['password']
    print('name = '+name)
    print('pwd = '+pwd)   
    return 'here is the data' 




def detail(request, question_id):
    return HttpResponse("You're looking at question %s" % question_id)


def results(request, question_id):
    response = "You're looking at the results of quesiton %s" % question_id
    return HttpResponse(response)

def vote(resuqest, question_id):
    return HttpResponse("You're voting on question %s" % question_id)
   

