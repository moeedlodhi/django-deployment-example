from django.shortcuts import render
from sixth_app import views
from sixth_app.forms import UserForm,UserProfile

from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout


def index(request):
    return render(request,'index.html')
# Create your views here.

def register(request):
    registered=False
    if request.method=='POST':
        mole=UserForm(data=request.POST)
        mole1=UserProfile(data=request.POST)
        if mole.is_valid() and mole1.is_valid():
            user = mole.save(commit=False)
            user.set_password(user.password)
            user.save()

            profile=mole1.save(commit=False)
            profile.user=user
            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']

            profile.save()
            registered=True
        else:
            print('Invalid form details')
    else:
        mole = UserForm()
        mole1 = UserProfile()
    return render(request,
                  'register.html',
                  {'registered':registered,'form':mole,'form1':mole1})

def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Account not active')

        else:
            return HttpResponse('User not available')

    else:
        return render(request, 'login.html')


@login_required()
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))











