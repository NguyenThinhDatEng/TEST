from dataclasses import field
from django import forms
from .models import Choice, Question


class PostQuestion(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title',)


class PostChoice(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ('answer', 'choices', )
