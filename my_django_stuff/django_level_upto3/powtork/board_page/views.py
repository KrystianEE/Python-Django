from django.shortcuts import render

# Create your views here.

def board(request):
    return render(request, 'board_page/page.html')
