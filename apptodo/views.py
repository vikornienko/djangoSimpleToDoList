from django.shortcuts import render

from .models import Todo

def todo_list(request):
    todos = Todo.objects.all()
    context_page = {
        "todo_list": todos
    }
    return render(request, 'index.html', context_page)

def todo_detail(request, id):
    todo = Todo.objects.get(id=id)
    context_page = {
        "todo": todo
    }
    return render(request, "detail.html", context_page)



