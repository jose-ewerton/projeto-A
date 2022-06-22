#from django.shortcuts import render
#from django.http import HttpResponse

from django.views.generic import TemplateView

# Create your views here.
'''
def view_home(request):
    return HttpResponse("Página Home")

def view_about(request):
    return HttpResponse("Página About")

def view_contact(request):
    return HttpResponse("Página Contacts")
'''

'''
def view_home(request):
    return render(request, "home.html")

'''
class HomeView(TemplateView):
    template_name = "base/home.html"



