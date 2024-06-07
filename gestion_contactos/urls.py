# gestion_contactos/urls.py

#from django.urls import path
#from .views import get_contacts

#urlpatterns = [
#    path('get_contacts/', get_contacts, name='get_contacts'),
#]

# gestion_contactos/urls.py

# gestion_contactos/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_contacts/', views.get_contacts, name='get_contacts'),
    path('add_contact/', views.add_contact, name='add_contact'),
    path('delete_contact/<int:contact_id>/', views.delete_contact, name='delete_contact'),
]
