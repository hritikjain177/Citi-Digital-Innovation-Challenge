from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/authentication/login')
def wordle(request):
    
   
    
    return render(request, 'wordle/wordle.html')
