from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context_dict = {'boldmessage': "I am bold font from the context"}
    #The second parameter concatinates the TEMPLATE_DIRS with the string in the parameter
    return render(request, 'rango/index.html', context_dict)

def about(request):
    context_dict = {'boldmessage': "I am bold from the context."}
    return render(request, 'rango/about.html', context_dict)