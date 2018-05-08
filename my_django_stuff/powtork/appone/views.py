from django.shortcuts import render
from django.http import HttpResponse
from appone.models import AccessRecord, Topic, Webpage
# Create your views here.


def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    return render(request, 'appone/index.html', context=date_dict)

def help(request):
    my_dict = {'insert': "No help sorry"}
    return render(request, 'appone/help.html', context=my_dict)
