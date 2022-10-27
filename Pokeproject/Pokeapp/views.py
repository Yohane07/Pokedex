from django.shortcuts import HttpResponse, render

# Create your views here.
def index(request):
    text = {"Oiseau":"pigeon"}
    return render(request, 'index.html', text)