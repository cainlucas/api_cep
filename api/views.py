from telnetlib import STATUS
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
import requests
# Create your views here.

def api_cep(request, cep):
    if len(cep) !=8:
        consulta_cep = {
            'cep': 'inválido'
        }
        return JsonResponse(consulta_cep, status=404)


    if len(cep) ==8:
        consulta_api = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        adress_data = consulta_api.json()
        return HttpResponse(json.dumps(adress_data, ensure_ascii=False, indent=2), content_type="application/json")



   # compilei um código em python para requisição de cep:

    # if'erro' not in adress_data:
    #     print('==>CEP ENCONTRADO<==')
    #     print('CEP:{}'.format(adress_data['cep']))
    #     print('Logradouro:{}'.format(adress_data['logradouro']))
    #     print('Complemento:{}'.format(adress_data['complemento']))
    #     print('Bairro:{}'.format(adress_data['bairro']))
    #     print('Cidade:{}'.format(adress_data['localidade']))
    #     print('Estado:{}'.format(adress_data['uf']))
    # else:
    #     print('{}: CEP inválido.'.format(cep_input))

    #     option = int(input('Deseja uma nova consulta?\n1. Sim\n2. Sair\n'))
    #     if option == 1:
    #         #main()
    #     #else:
    #         print('Saindo...')
    #     #if __name__ == '__main__':
    #         #main()