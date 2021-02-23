from django.shortcuts import render, HttpResponse

# Create your views here.
# urls dispatching
def index(request) :
    context = {
        'message': 'Hello World!'
    }
    return render(request , 'index.html', context)
    
def about(request) :
    return render(request , 'about.html')
    
def contact(request) :
    return render(request , 'contact.html')
