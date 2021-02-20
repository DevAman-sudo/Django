from django.shortcuts import render, HttpResponse

# Create your views here.
# urls dispatching
def index(request) :
    return HttpResponse("this is devaman")
    
def about(request) :
    return HttpResponse("this is about page")
    
def contact(request) :
    return HttpResponse("this is contact page")
    