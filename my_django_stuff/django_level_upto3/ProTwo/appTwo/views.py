from django.shortcuts import render
from appTwo.models import User
from . import forms
# Create your views here.



def index(request):
    return render(request, 'appTwo/index.html')


def users(request):
    form = forms.UserLog()

    if request.method == 'POST':

        form = forms.UserLog(request.POST)

        if form.is_valid():
            new_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_email = form.cleaned_data['email']
            temp = temp_user=User.objects.get_or_create(first_name=new_name, last_name=new_last_name, email=new_email)

    return render(request, 'appTwo/users.html', {'form' : form})
