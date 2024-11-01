from django.shortcuts import render
from django.contrib.auth.forms import UserChangeForm
# Create your views here.

def register(request):
    register_form = UserChangeForm()
    context={
        'register_form': register_form
    }
    return render(request, 'register.html',context)
