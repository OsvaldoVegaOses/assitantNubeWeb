# api/urls.py

#from django.urls import path
#from .views import api_overview

#urlpatterns = [
#    path('', api_overview, name='api_overview'),
#]

# api/urls.py
# api/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('handle_request/', views.handle_request, name='handle_request'),
]

