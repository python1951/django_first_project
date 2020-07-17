from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecord,Topic,WebPage
from first_app import forms

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
