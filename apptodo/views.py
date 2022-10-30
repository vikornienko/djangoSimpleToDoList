from django.shortcuts import render

from .models import Todo

def todo_list(request):
    todos = Todo.objects.all()
    context_page = {
        "todo_list": todos
    }
    return render(request, 'index.html', context_page)

