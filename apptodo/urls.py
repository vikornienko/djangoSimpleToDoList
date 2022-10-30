from django.urls import path

from .views import todo_list

app_name = 'apptodo'

urlpatterns = [
    path('', todo_list),
]