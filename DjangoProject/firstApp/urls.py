from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello),
    path('questions/', views.listOfQuestions),
    path('questions/<int:id>', views.questionDetails),
]
