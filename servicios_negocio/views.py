#primer bloque d codigo de prueba anulado por segundo bloque
#from django.shortcuts import render
# servicios_negocio/views.py

#from django.http import JsonResponse

#def get_services(request):
#    services = {
#        "design": "Diseño gráfico, branding y diseño de interfaces.",
#        "development": "Desarrollo de sitios web, aplicaciones web y e-commerce.",
#        "content_creation": "Generación de contenido, redacción SEO y marketing de contenidos.",
#        "consulting": "Asesoría en estrategias digitales y mejoras de rendimiento web."
#    }
#    return JsonResponse(services)

# gestion_contactos/views.py

#segundo bloque de codigo anulado por tercr bloque
#from django.shortcuts import render
#from django.http import HttpResponse

#def index(request):
#    return HttpResponse("Página de gestión de contactos")

#def get_contacts(request):
#    return HttpResponse("Lista de contactos")

# servicios_negocio/views.py

from django.http import JsonResponse, HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return HttpResponse("Página de servicios de negocio")

def service_info(request):
    # Simula la información de los servicios de negocio
    data = {"service1": "Información del servicio 1", "service2": "Información del servicio 2"}
    return JsonResponse(data)

@csrf_exempt
def add_service(request):
    if request.method == "POST":
        data = json.loads(request.body)
        # Aquí puedes procesar y guardar la información del servicio
        return JsonResponse({"message": "Servicio agregado", "data": data})


