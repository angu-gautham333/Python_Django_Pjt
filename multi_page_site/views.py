from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def result(request):
    user_input = request.GET['user_input']
    user_input += " is the entered string in the Home page"
    return render(request, 'result.html', {'home_input':user_input})
