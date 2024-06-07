# gestion_contactos/views.py

#from django.shortcuts import render
#from django.http import JsonResponse
#from .models import Contact

#def get_contacts(request):
#    contacts = Contact.objects.all().values('name', 'email', 'message')
#    return JsonResponse(list(contacts), safe=False)

# gestion_contactos/views.py

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Página de gestión de contactos")

#def get_contacts(request):
#    return HttpResponse("Lista de contactos")

# gestion_contactos/views.py

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from .models import Contact
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    return HttpResponse("Página de gestión de contactos")

def get_contacts(request):
    contacts = Contact.objects.all()
    data = [{"name": contact.name, "email": contact.email, "phone": contact.phone} for contact in contacts]
    return JsonResponse(data, safe=False)

@csrf_exempt
def add_contact(request):
    if request.method == "POST":
        data = json.loads(request.body)
        contact = Contact.objects.create(name=data["name"], email=data["email"], phone=data.get("phone"))
        return JsonResponse({"id": contact.id, "name": contact.name, "email": contact.email, "phone": contact.phone})

@csrf_exempt
def delete_contact(request, contact_id):
    if request.method == "DELETE":
        contact = get_object_or_404(Contact, id=contact_id)
        contact.delete()
        return JsonResponse({"message": "Contact deleted"})

