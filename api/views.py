#primer bloque anulado por segundo bloque
##from django.shortcuts import render
## api/views.py

#from django.http import JsonResponse

#def api_overview(request):
#    api_urls = {
#        'get_contacts': '/gestion_contactos/get_contacts/',
#        'get_services': '/servicios_negocio/get_services/',
#        'send_contact_email': '/envio_correos/send_contact_email/',
#    }
#    return JsonResponse(api_urls)

# api/views.py

#segundo bloque anulado por tercer bloque
#from django.shortcuts import render
#from django.http import HttpResponse

#def index(request):
#    return HttpResponse("Página de API")

# api/views.py

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    return HttpResponse("Página de API")

@csrf_exempt
def handle_request(request):
    if request.method == "POST":
        data = json.loads(request.body)
        # Aquí puedes manejar la lógica específica de los endpoints RESTful
        return JsonResponse({"message": "Request handled", "data": data})
