# envio_correos/urls.py

#from django.urls import path
#from .views import send_contact_email

#urlpatterns = [
#    path('send_contact_email/', send_contact_email, name='send_contact_email'),
#]

# servicios_negocio/urls.py

# envio_correos/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('send_email/', views.send_email, name='send_email'),
]

