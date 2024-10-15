from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    form = RegisterForm()
    return render(request,'register.html',{'form':form})
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                              username=cd['username'],
                              password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('list')
    form = LoginForm()
    return render(request,'login.html',{'form':form})

def logout_view(request):
    logout(request)
    return redirect('users:login')
