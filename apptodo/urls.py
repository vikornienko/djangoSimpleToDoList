from django.urls import path

from .views import todo_list, todo_detail, todo_create, todo_update, todo_delete

app_name = 'apptodo'

urlpatterns = [
    path('', todo_list),
    path('create/', todo_create),
    path('<int:id>/', todo_detail),
    path('<int:id>/update', todo_update),
    path('<int:id>/delete', todo_delete),
]
