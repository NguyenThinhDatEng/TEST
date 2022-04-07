from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Question(models.Model):
    title = models.CharField(max_length=100, null=False)

    def __str__(self) -> str:
        return self.title


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # on_delete=models.CASCADE
    # when the question is removed, the choice also is deleted
    answer = models.TextField(max_length=100, null=False)
    choices = models.IntegerField(default=0)

# customize user in django


class User(AbstractUser):
    sex_choices = ((0, 'Male'), (1, 'Female'), (2, 'Unknown'))
    phone_number = models.CharField(max_length=11, null=False)
    # choices = object
    sex = models.IntegerField(choices=sex_choices, default=0)
