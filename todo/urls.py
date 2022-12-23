from django.urls import path
from .views import Cred

urlpatterns = [
    path('<int:pk>/', Cred.as_view()),
]
