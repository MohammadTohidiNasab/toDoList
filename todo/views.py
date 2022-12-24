from rest_framework import generics
from .serializers import ToDoSerializer
from .models import Todo

class Cred (generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = ToDoSerializer
class ListTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = ToDoSerializer

class CreateTodo(generics.CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = ToDoSerializer
