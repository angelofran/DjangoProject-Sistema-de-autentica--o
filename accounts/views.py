from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate


def signUp(request):
    if request.user.is_authenticated:
        return redirect('/accounts/home')
    if request.method == "GET":
        return render(request, 'signup.html')
    
    else:
        nome = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('password')

        if len(nome.strip()) == 0 or len(email.strip()) == 0 or len(senha.strip()) == 0:
    
            return render(request, 'signup.html')

        try:
            user = User.objects.create_user(
                username=nome,
                email=email,
                password=senha,
            )
            return redirect('/accounts/login/')
        except Exception as err:
            print(err)
            return render(request, 'signup.html')


def logIn(request):
    if request.method == "GET":
        return render(request, 'login.html')
    
    elif request.method == "POST":
        nome = request.POST.get('username')
        senha = request.POST.get('password')
        user = authenticate(username=nome, password=senha)
        if user is not None:
            login(request, user)
            return redirect('/accounts/home')
        else:
            return render(request, 'login.html')
        

def logOut(request):
    logout(request)
    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html', {'nome':request.user.username})


