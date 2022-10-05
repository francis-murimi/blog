from django.shortcuts import render,get_object_or_404,redirect
from django.template import loader
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import ExtendedUserCreationForm,UserProfileForm,LoginForm
from .models import UserProfile
from django.contrib.auth.models import User

def user_register(request):
    template = loader.get_template('profiles/register.html')
    if request.method == 'POST':
        form =ExtendedUserCreationForm(request.POST) # user creation form
        profile_form = UserProfileForm(request.POST) # userprofile creation form
        
        if form.is_valid() and profile_form.is_valid(): # validate both forms
            user = form.save()
            profile = profile_form.save(commit=False) # save form without committing to the database
            profile.profile_owner = user
            profile.first_name = user.first_name
            profile.last_name = user.last_name
            
            profile.save()
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1') 
            user = authenticate(username=username,password=password) # log in the created user
            login(request,user)
            return redirect('blogger:homePage')
    else:
        form = ExtendedUserCreationForm()
        profile_form = UserProfileForm()
    
    context = {'form':form,'profile_form':profile_form}
    return HttpResponse(template.render(context,request))


def log_in(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect ('blogger:homePage')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
        else:
            form = LoginForm()
    form = LoginForm()
    template = loader.get_template('profiles/login.html')
    context = {'form':form}
    return HttpResponse(template.render(context,request))

def log_out(request):
    logout(request)
    return redirect('blogger:homePage')