from django.urls import path
from . import views
urlpatterns = [
    path('todolist', views.todolist),
    path('todoitem/<str:pk>', views.todoitem)
]