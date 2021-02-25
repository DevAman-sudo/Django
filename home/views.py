from django.shortcuts import render, HttpResponse
from home.models import Contact

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
    if request.method == "POST" :
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = Contact(name = name , email = email)
        contact.save()
        
    return render(request , 'contact.html')