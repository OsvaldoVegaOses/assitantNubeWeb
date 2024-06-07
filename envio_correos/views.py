#primer bloque de código anulado por segundo bloque
## envio_correos/views.py
#rom django.shortcuts import render
#from django.http import JsonResponse
#from django.views.decorators.http import require_POST
#from .utils import send_email
#from django.views.decorators.csrf import csrf_exempt

#@csrf_exempt
#@require_POST
#def send_contact_email(request):
#    to_email = request.POST.get('to_email')
#    subject = request.POST.get('subject')
#    body = request.POST.get('body')
#    
#    if send_email(to_email, subject, body):
#        return JsonResponse({'message': 'Correo enviado exitosamente.'})
#    else:
#        return JsonResponse({'message': 'Error al enviar el correo.'}, status=500)

# envio_correos/views.py
#segundo bloque anulado por tercer bloque
#from django.shortcuts import render
#from django.http import HttpResponse

#def index(request):
#    return HttpResponse("Página de envío de correos")

# envio_correos/views.py

from django.http import JsonResponse, HttpResponse
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    return HttpResponse("Página de envío de correos")

@csrf_exempt
def send_email(request):
    if request.method == "POST":
        data = json.loads(request.body)
        send_mail(
            data["subject"],
            data["message"],
            'from@example.com',
            [data["to"]],
            fail_silently=False,
        )
        return JsonResponse({"message": "Email sent"})

