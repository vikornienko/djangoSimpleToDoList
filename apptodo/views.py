from django.shortcuts import render
from django.http import HttpResponse

def todo_list(request):
    return render(request, 'index.html')

