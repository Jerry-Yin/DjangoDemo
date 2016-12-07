from django.conf.urls import url

from . import views
from myapp import views


urlpatterns = [
    # ex: /myapp/
    url(r'^$', views.index, name='index'),
    # ex: /myapp/5
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /myapp/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'), 
    # ex: /myapp/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
   
]
