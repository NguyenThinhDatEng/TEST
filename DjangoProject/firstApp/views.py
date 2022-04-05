from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import Question
from .forms import PostQuestion, Email

# function base view


class Index(View):
    def get(self, request):
        parameters = {'name': 'Nguyen Van Thinh', 'technology': [
            'Linux', 'Docker', 'Jdpaint', 'Python', 'Octave']}
        return render(request, 'firstApp/index.html', parameters)

# Question


def listOfQuestions(request):
    questions = Question.objects.all()
    parameters = {'questions': questions}
    return render(request, 'firstApp/question/questions.html', parameters)


def questionDetails(request, id):
    try:
        question = Question.objects.get(pk=id)
    except:
        question = ''
    return render(request, 'firstApp/question/question_details.html', {'question': question})


def showChoices(request, question_id):
    question = Question.objects.get(pk=question_id)
    data = request.POST['choice']
    choice = question.choice_set.get(pk=data)
    choice.choices += 1
    choice.save()
    return render(request, 'firstApp/question/voting_results.html', {'question': question})


def addForm(request):
    question = PostQuestion()
    return render(request, 'firstApp/question/addQuestion.html', {'questionObj': question})


def saveQuestion(request):
    if request.method == 'POST':
        # get data
        question = PostQuestion(request.POST)  # type casting
        # save question to database
        question.save()
        return HttpResponse('Save successfully')
    else:
        return HttpResponse('Wrong method')

# Email


def write(request):
    email = Email()
    return render(request, 'firstApp/email/write.html', {'email': email})


def showLetter(request):
    if request.method == 'POST':
        data = Email(request.POST)
        print(data)
        if data.is_valid():
            # email = data.cleaned_data['to']
            letter = data.cleaned_data
            # now in the object letter, you have the form as a dictionary.
            return render(request, 'firstApp/email/showLetter.html', {'letter': letter})
        else:
            return HttpResponse('Wrong fromat')
    else:
        return HttpResponse('Wrong method')
