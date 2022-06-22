from django.urls import path
from .views import HomeView #view_home, view_about, view_contact


urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
    #path('home/', view_home ),
    #path('about/', view_about),
    #path('contact/', view_contact),
]