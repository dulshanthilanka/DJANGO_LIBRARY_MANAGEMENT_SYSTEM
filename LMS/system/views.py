from django.shortcuts import render, redirect
from . form import SignupForm
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def signupBook(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
    else:
        form = SignupForm()

    return render(request, 'system/signupForBorrow.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginroute')
    else:
        form = UserCreationForm()

    return render(request, 'system/UserSignup.html', {'form': form})