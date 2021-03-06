from django.shortcuts import render, redirect
from .models import User, UserManager
from django.contrib import messages
from django.core.urlresolvers import reverse
from .forms import RegisterForm

def index(request):
    form = RegisterForm()
    context = { "regForm": form }
    return render(request, 'login/index.html', context)

def create(request):
    first_name=str(request.POST['first_name'])
    last_name=str(request.POST['last_name'])
    email=str(request.POST['email'])
    password1=str(request.POST['password1'])
    password2=str(request.POST['password2'])
    valid, response = User.userManager.validate(first_name, last_name, email, password1, password2)
    if valid:
        context = {
            'event': 'registered',
            'first_name': response
        }
        return render(request, 'login/success.html', context)
    elif not valid: 
        messages.error(request, response)
    else:
        messages.error(request, "Something went wrong. Try again later.")
    return redirect(reverse('home'))
    
##TODO: change routing so successful login/register redirects to /success 
def login(request):
    email = str(request.POST['email'])
    password = str(request.POST['password'])
    valid, response = User.userManager.login(email, password)
    if valid:
        context = {
            'event': "logged in",
            'first_name': response,
        }
        return render(request, 'login/success.html', context)
    if not valid:
        messages.error(request, response)
        return redirect(reverse('home'))

