from django.shortcuts import render

# Create your views here.


def index(request):
    dict1={'insert_content': 'hello im form app12'}
    return render(request, 'app12/index.html', context=dict1)
