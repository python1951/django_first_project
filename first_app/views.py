from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecord,Topic,WebPage,Login
from first_app import forms
from first_app.forms import UserForm,UserFormm,UserProfileInfoForm
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from  django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('success'))
@login_required
def special(request):
    return HttpResponse("Yadd atey ho bohat...login kr to ateyy...")

def index(request):
    acc_recrd = AccessRecord.objects.order_by("date")
    date_dict = {"access_records":acc_recrd}
    pass
    return render(request, 'first_app/index.html', context = date_dict)
def form_view(request):
    form = forms.FormName()
    if (request.method == "POST"):
        form = forms.FormName(request.POST)
        if(form.is_valid()):
            print("Name is "+form.cleaned_data["name"]),
            print("Email is "+form.cleaned_data["email"]),
            print("Text is "+form.cleaned_data["text"]),
    return render(request, 'first_app/form.html', {"form":form})

def login_view(request):
    form_login = forms.UserForm()
    if(request.method == "POST"):
        form_login = forms.UserForm(request.POST)
        if form_login.is_valid():
            form_login.save(commit=True)

    return render(request,'first_app/login.html',{"login_form":form_login})
def success_view(request):
    context_dict = {"body":"hello man we are very happy to help you","number":100}
    return render(request,'first_app/success.html',context=context_dict)
def extended(request):
    return render(request,'first_app/extended.html')
def register(request):
    registered = False
    if (request.method == 'POST'):
        user_form = UserFormm(data = request.POST)
        profile_form = UserProfileInfoForm(data = request.POST)
        if( user_form.is_valid() and profile_form.is_valid()):
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user # representing one to one relationship
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserFormm()
        profile_form = UserProfileInfoForm()
    return render(request,'first_app/registration.html',{'user_form':user_form,'profile_info':profile_form,'registered':registered})
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('success'))
            else:
                return HttpResponse("NO user found")
        else:
            print("Invalid creds")
            print("username is {} an password is {}".format(username,password))
    else:
        return render(request,'first_app/loginn.html')
