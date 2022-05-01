from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.





@login_required(login_url='/authentication/login')
def sips(request):
   
    return render(request, 'investment/sips.html')



@login_required(login_url='/authentication/login')
def stocks(request):
   
    return render(request, 'investment/mutualfunds.html')