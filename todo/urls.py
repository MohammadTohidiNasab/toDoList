from django.urls import path
from .views import Cred, ListTodo, CreateTodo

urlpatterns = [
    path('<int:pk>/', Cred.as_view(),name='cred'),
    path('', ListTodo.as_view()),
    path('create', CreateTodo.as_view(),name='create'),
]
