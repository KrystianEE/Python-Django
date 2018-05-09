from django.shortcuts import render
from . import forms
# Create your views here.

def index(request):
    return render(request, "testapp/index.html")


def formpage(request):
    form = forms.FormName()
    #return render(request, 'testapp/formpage.html', {'form' : form})

    if request.method == 'POST' :
        form = forms.FormName(request.POST)


        if form.is_valid():
            print('NAME: '+form.cleaned_data['name'])
            print('EMIAL: '+form.cleaned_data['email'])
            print('TExT: '+form.cleaned_data['text'])

    return render(request, 'testapp/formpage.html', {'form':form})
