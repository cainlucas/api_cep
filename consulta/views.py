from django.shortcuts import render
from django.http import HttpResponse
from api.models import Meucep

# Create your views here.

def print (request):

    cep = request.GET.get('cep')

    if str(cep).isnumeric():
    # if request.method=='GET':
        endereco = Meucep.objects.get(cep=cep)
        context = {
            'cep':endereco.cep,
            'cidade':endereco.cidade,
            'bairro':endereco.bairro,
            'rua':endereco.rua,
        }
        # print(endereco)
        return render (request, 'consulta.html',{'resposta_consulta':context})
    else:
        return render (request, 'consulta.html')