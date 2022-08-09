from urllib import response
import requests

def test_status_code():
    link_site = 'https://busercep.herokuapp.com/'
    response = requests.get(link_site)
    assert response.status_code == 200

def test_cep():
    link_site = 'https://busercep.herokuapp.com/api/cep/05641900'
    response = requests.get(link_site).json()
    assert response == {
    "cep": "05641-900",
    "logradouro": "Rua Marechal Hastinfilo de Moura",
    "complemento": "338",
    "bairro": "Vila Suzana",
    "localidade": "São Paulo",
    "uf": "SP",
    "ibge": "3550308",
    "gia": "1004",
    "ddd": "11",
    "siafi": "7107"
    }