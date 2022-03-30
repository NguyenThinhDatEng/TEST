from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from .forms import PostQuestion, PostChoice


def hello(request):
    # return HttpResponse('Hello owner, I am here')
    parameters = {'name': 'Nguyen Van Thinh', 'technology': [
        'Linux', 'Docker', 'Jdpaint', 'Python', 'Octave']}
    return render(request, 'firstApp/index.html', parameters)


def listOfQuestions(request):
    questions = Question.objects.all()
    parameters = {'questions': questions}
    return render(request, 'firstApp/questions.html', parameters)


def questionDetails(request, id):
    try:
        question = Question.objects.get(pk=id)
    except:
        question = ''
    return render(request, 'firstApp/question_details.html', {'question': question})


def showChoices(request, question_id):
    question = Question.objects.get(pk=question_id)
    data = request.POST['choice']
    choice = question.choice_set.get(pk=data)
    choice.choices += 1
    choice.save()
    return render(request, 'firstApp/voting_results.html', {'question': question})


def addForm(request):
    question = PostQuestion()
    return render(request, 'firstApp/addQuestion.html', {'questionObj': question})


def saveQuestion(request):
    if request.method == 'POST':
        # get data
        req = request.POST
        # create a new question
        try:
            heading = req['title']
        except KeyError:
            print('No Key Found')
        try:
            question = Question(title=heading)
        except:
            print('SOS')
        # save question to database
        question.save()
        return HttpResponse('Save successfully')
    else:
        return HttpResponse('Wrong method')
