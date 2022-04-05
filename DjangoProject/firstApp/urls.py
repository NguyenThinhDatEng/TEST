from django.urls import path
from . import views

# because many applications have the same view names
# {% url 'app:view' %}

app_name = 'firstApp'

urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('questions/', views.listOfQuestions, name='list'),
    path('questions/<int:id>', views.questionDetails, name='detail'),
    path('choices/<int:question_id>', views.showChoices, name='choices'),
    # path('addQuestion', views.addForm, name='add'),
    path('save', views.SaveQuestion.as_view(), name='save'),    # merge add question and save
    path('write', views.write, name='write'),
    path('letter', views.showLetter, name='letter'),
]
