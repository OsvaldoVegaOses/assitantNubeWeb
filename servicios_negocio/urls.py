# servicios_negocio/urls.py

#from django.urls import path
#from .views import get_services

#urlpatterns = [
#    path('get_services/', get_services, name='get_services'),
#]

# servicios_negocio/urls.py

# servicios_negocio/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('service_info/', views.service_info, name='service_info'),
    path('add_service/', views.add_service, name='add_service'),
]

