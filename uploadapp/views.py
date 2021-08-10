from django.shortcuts import render,redirect
from .forms import StudentsDetailsForm,Login
from django.http import HttpResponse,JsonResponse
from .models import StudentsDeails
from django.contrib.auth.decorators import login_required
# Create your views here.


def StudentDetailsView(request):

    if request.method=="POST":
        forms=StudentsDetailsForm(request.POST,request.FILES)
        if forms.is_valid():
            forms.save()
            return redirect('/')
    else:
        forms=StudentsDetailsForm()
    return render(request,'uploadapp/register.html',{'forms':forms})

def GetInfoView(request):
    if request.method=='POST':
        forms=Login(request.POST)
        if forms.is_valid():
            email=forms.cleaned_data['email']
            password=forms.cleaned_data['password']
            getinfo=StudentsDeails.objects.filter(email__exact=email)
            if getinfo[0].password==password:
                return render(request,'uploadapp/getinfo.html',{'getinfo':getinfo})
    else:
        forms=Login()
    return render(request,'uploadapp/getinfo.html',{'forms':forms})

def getAll(request):
    obj=StudentsDeails.objects.all()
    res={"details":list(obj.values('name','age','phone','email'))}
    return JsonResponse(res)