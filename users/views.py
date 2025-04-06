from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .forms import LoginForm, RegisterForm
from django.http import HttpResponse

class LoginView(View):
    def get(self,request):
        form = LoginForm()
        return render(request, 'login.html',{'form':form})
    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect("home")
            else:
                message = 'Login yoki parol xato!'
                return render(request, 'login.html',{'form':form,'message':message})
        else:
            message = 'Kataklarni to\'ldiring!'
            return render(request, 'login.html',{'form':form,'message':message})
    
class RegisterView(View):
    def get(self,request):
        form = RegisterForm()
        return render(request, 'register.html',{'form':form})
    def post(self,request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            if form.cleaned_data["checkmark"] == True:
                user = User(
                    username = form.cleaned_data["username"],
                    first_name = form.cleaned_data["first_name"],
                    last_name = form.cleaned_data["last_name"],
                    email = form.cleaned_data["email"],
                )
                user.set_password(form.cleaned_data["password"])
                user.save()
                login(request,user)
                return redirect('home')
            else:
                message = 'Roziman ni bosing!'
            return render(request, 'register.html',{'form':form,'message':message})
        else:
            message = 'Kataklarni to\'ldiring!'
            return render(request, 'register.html',{'form':form,'message':message})
    
def logout(request):
    logout(request)
    redirect('home')