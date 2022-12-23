from rest_framework import generics
from .serializers import ToDoSerializer
from .models import Todo

class Cred (generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = ToDoSerializer
