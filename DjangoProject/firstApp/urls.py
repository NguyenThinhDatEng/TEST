from secrets import choice
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='home'),
    path('questions/', views.listOfQuestions, name='list'),
    path('questions/<int:id>', views.questionDetails, name='detail'),
    path('choices/<int:question_id>', views.choicesOfQuestion, name='choices')
]
