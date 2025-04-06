from django.shortcuts import render, get_object_or_404, redirect
from users.models import User
from django.views import View
from django.http import HttpResponse
from .forms import AmountForm, CardInfoForm
from .models import Transaction

class IndexView(View):
    def get(self,request):
        return render(request, 'index.html')

class DonatePageView(View):
    def get(self,request,username):
        user = get_object_or_404(User,username=username)
        form = AmountForm()
        return render(request, 'author-page.html', {"author":user})
    def post(self,request,username):
        user = get_object_or_404(User,username=username)
        form = AmountForm(request.POST)
        if form.is_valid():
            transaction = Transaction(
                sender = form.cleaned_data["name"],
                author = user,
                amount = form.cleaned_data["amount"],
                status = False
            )
            transaction.save()
            return redirect("payment", id=transaction.id)

class PaymentView(View):
    def get(self,request,id):
        form = CardInfoForm()
        return render(request, 'payment.html', {"form":form})
    def post(self,request,id):
        transaction = get_object_or_404(Transaction,id=id)
        form = CardInfoForm(request.POST)
        if form.is_valid():
            card = str(form.cleaned_data["card"]).replace(" ",'')
            month = form.cleaned_data["month"]
            year = int(form.cleaned_data["year"])
            print(card, month, year)
            if len(card) == 16 and len(month) == 2 and len(str(year)) == 2 and year > 25 and year < 40:
                transaction.card = card
                transaction.valid = f'{month}/{year}'
                transaction.status = True
                transaction.save()
                return redirect("home")
            else:
                message = "Ma\'lumotlarda xatolik bor!"
                return render(request, 'payment.html', {"form":form,"message":message})
        return render(request, 'payment.html', {"form":form})
    
class AuthorsView(View):
    def get(self,request):
        users = User.objects.all()
        return render(request, "authors.html",{"users":users})