from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'welcome.html',{})
def disclaimer(request):
    return render(request,'disclaimer.html',{})
def termsConditions(request):
    return render(request,'terms_conditions.html',{})
def codeOfEthics(request):
    return render(request,'codeofethics.html',{})