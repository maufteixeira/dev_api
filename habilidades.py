from flask import Flask, request
from flask_restful import Resource, Api
import json


app = Flask(__name__)
api = Api(app)

lista_habilidades = [
    'html', 'CSS',
    'flask', 'Python'
]


class Habilidades(Resource):

    def get(self, posicao):
        try:
            response = lista_habilidades[posicao]
        except IndexError:
            mensagem = 'Habilidade id{} nao exite'.format(posicao)
            response = {'Status:': 'Erro', 'Mensagem:': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o ADMIN'
            response = {'Status:': 'Erro', 'Mensagem:': mensagem}
        return response


    def put(self, posicao):
        dados = json.loads(request.data)
        lista_habilidades[posicao] = dados
        return dados

    def delete(self, posicao):
        lista_habilidades.pop(posicao)
        return {'status': 'sucesso', 'mensagem': 'Registro excluido'}

class ListaHabilidades(Resource):
    def get(self):
        return lista_habilidades

    def post(self):
        dados = json.loads(request.data)
        posicao = len(lista_habilidades)
        dados['id'] = posicao
        lista_habilidades.append(dados)
        return lista_habilidades[posicao]
