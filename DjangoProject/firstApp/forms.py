from django import forms
from .models import Question

# widget -> add class, id, ... for attributes

# model forms


class PostQuestion(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'titleQues', 'id': 'test01'})
        }

# form no model


class Email(forms.Form):
    title = forms.CharField(max_length=100, required=True,
                            widget=forms.TextInput(attrs={'class': 'titleQues'}))
    to = forms.EmailField(
        required=True, widget=forms.TextInput(attrs={'class': 'email'}))
    content = forms.CharField(required=True, widget=forms.Textarea(
        attrs={'class': 'contentEmail'}))
