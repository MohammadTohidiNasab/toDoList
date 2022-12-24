from django.urls import path
from .views import Cred, ListTodo, CreateTodo

urlpatterns = [
    path('<int:pk>/', Cred.as_view()),
    path('', ListTodo.as_view()),
    path('create', CreateTodo.as_view()),
]
