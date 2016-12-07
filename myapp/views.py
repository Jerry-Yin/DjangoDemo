from django.shortcuts import render, get_object_or_404
from django.template import loader, RequestContext
from django.http import HttpResponse, Http404

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
    template = loader.get_template('myapp/index.html')
    #output = ', '.join([p.question_text for p in latest_question_list])
    context = RequestContext(request, {
        'latest_question_list': latest_question_list,    
    })
    return HttpResponse(template.render(context))


def getdata(request):
    name = request.POST['username']
    pwd = request.POST['password']
    print('name = '+name)
    print('pwd = '+pwd)   
    return 'here is the data' 




def detail(request, question_id):
    template = loader.get_template('myapp/detail.html')
    #try:
    #    question = Question.objects.get(pk=question_id)
    #except Question.DoesNotExist:
    #    raise Http404("Question %s does not exist" % question_id)
    #context = "You're looking at question %s" % question_id
    
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question
    }
    return HttpResponse(template.render(context, request))


def results(request, question_id):
    response = "You're looking at the results of quesiton %s" % question_id
    return HttpResponse(response)

def vote(resuqest, question_id):
    return HttpResponse("You're voting on question %s" % question_id)
   

