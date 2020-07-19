from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecord,Topic,WebPage,Login
from first_app import forms
from first_app.forms import UserForm

# Create your views here.
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
