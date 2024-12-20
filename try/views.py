from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db.models.expressions import result
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from .models import Question, User, UserAnswer


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return redirect('home1')
    questions = Question.objects.all()
    return render(request, 'home.html', {'questions': questions})

@login_required
def home1(request):
    user = request.user
    questions = Question.objects.all()
    return render(request, 'home1.html', {'questions': questions, 'user': user})

def correction(request):
    return render(request, 'correction.html')

def inscription(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            # Vérifier si l'utilisateur existe déjà
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists. Please choose a different one.")
            else:
                # Enregistrer l'utilisateur
                user = form.save()
                # Authentifier et connecter l'utilisateur
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, f"Welcome {username}, your account has been successfully created!")
                    return redirect('home')  # Redirige vers la page d'accueil après inscription
        else:
            messages.error(request, 'Something went wrong. Please try again.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'inscription.html', {'form': form})

def conection(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        if not username or not password:
            messages.error(request, 'Both username and password are required!')
            return render(request, 'conection.html')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome {username}!")
            return redirect('home')
        else:
            messages.error(request, 'Username or password is incorrect!')
    return render(request, 'conection.html')

@login_required
def profile(request):
    user = request.user
    return render(request, 'profile.html', {"user": user})

@login_required
def submit_answers(request):
    if request.method == 'POST':
        user = request.user
        score = 0
        result = []

        for question in Question.objects.all():
            question_id = str(question.id)
            user_answer = request.POST.get(question_id, '').strip()
            is_correct = user_answer.lower() == question.correct_answer.lower()

            UserAnswer.objects.create(
                user=user,
                question=question,
                answer=user_answer,
                is_correct=is_correct
            )

            result.append({
                'question': question,
                'user_answer': user_answer,
                'correct_answer': question.correct_answer,
                'is_correct': is_correct
            })

            if is_correct:
                score += 1

        return render(request, 'correction.html', {
            'results': result,  # Modifiez "result" par "results" pour correspondre au template
            'score': score,
            'total_questions': Question.objects.count()
        })
    else:
        return redirect('home1')

