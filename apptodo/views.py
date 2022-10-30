from django.shortcuts import render, redirect

from .models import Todo
from .forms import TodoForm

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

def todo_create(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    context_page = {
        "form": form
    }
    return render(request, "create.html", context_page)



