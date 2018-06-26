from django.conf.urls import url
from . import views

app_name = 'pollsapp'

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^(?P<question_id>[0-9]+)/$', views.qsns, name='qsns'),
    url(r'^(?P<question_id>[0-9]+)/vote$', views.vote, name='vote'),
    url(r'^(?P<question_id>[0-9]+)/result$', views.result, name='result'),
]
