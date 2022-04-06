from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate, login, decorators
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Question
from .forms import PostQuestion, Email

# function base view


class Index(View):
    def get(self, request):
        parameters = {'name': 'Nguyen Van Thinh', 'technology': [
            'Linux', 'Docker', 'Jdpaint', 'Python', 'Octave']}
        return render(request, 'firstApp/index.html', parameters)

# Question
# request.POST is a dictionary


class SaveQuestion(View):
    def get(self, request):
        question = PostQuestion()
        return render(request, 'firstApp/question/addQuestion.html', {'questionObj': question})

    def post(self, request):
        # get data
        question = PostQuestion(request.POST)  # type casting
        # save question to database
        question.save()
        return HttpResponse('Save successfully')


@decorators.login_required(login_url='/login')  # decorator
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

# Login


class Login(View):
    def get(self, request):
        return render(request, 'firstApp/login/login.html')

    def post(seft, request):
        username = request.POST['username']
        password = request.POST['password']
        customer = authenticate(username=username, password=password)
        if customer is None:
            return HttpResponse('Customer does not exist')
        # Persist a user id and a backend in the request
        # user doesn't have to reauthenticate on every request
        login(request, customer)
        return HttpResponse(f'Login successfully!')

# must put LoginRequiredMixin before View


class ViewOfUser(LoginRequiredMixin, View):
    login_url = '/login'

    def get(self, request):
        # if request.user.is_authenticated:
        return HttpResponse('<h1>The view of user!')
