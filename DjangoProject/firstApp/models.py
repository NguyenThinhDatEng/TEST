from django.db import models

# Create your models here.
class Question(models.Model):
    id = models.IntegerField
    content = models.TextField(max_length=100)
     
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # on_delete=models.CASCADE
    # when the question is removed, the choice also is deleted
    answer = models.TextField(max_length=100)
    choices = models.IntegerField(default=0)