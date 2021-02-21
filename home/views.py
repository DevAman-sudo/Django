from django.shortcuts import render, HttpResponse

# Create your views here.
# urls dispatching
def index(request) :
    context = {
        'message': 'Hello World!'
    }
    return render(request , 'index.html', context)
    
def about(request) :
    return HttpResponse("this is about page")
    
def contact(request) :
    return HttpResponse("this is contact page")
    