from flask import Flask, request
from flask_restful import Resource, Api
import json
from habilidades import Habilidades, ListaHabilidades
app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {
        'id': 0,
        'name': 'Mauricio',
        'Habilidade': ['html', 'CSS']
    },
    {
        'id': 1,
        'name': 'Pedro',
        'Habilidade': ['flask', 'Python']
    }
]


class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de id{} nao exite'.format(id)
            response = {'Status:': 'Erro', 'Mensagem:': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o ADMIN'
            response = {'Status:': 'Erro', 'Mensagem:': mensagem}
        return response


    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status': 'sucesso', 'mensagem': 'Registro excluido'}


class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]


api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Habilidades, '/habilidades/<int:posicao>/')
api.add_resource(ListaHabilidades, '/habilidades/')

if __name__ == '__main__':
    app.run(debug=True)