from flask import Flask, jsonify, request
import json


app = Flask(__name__)


desenvolvedores = [{'id':0,'name': 'Mauricio',
'Habilidade':['html', 'CSS']},
{'id':1, 'name':'Pedro', 'Habilidade':['flask', 'Python']}
                   ]

#Retorna um desenvolvedor pelo ID, também modifca e exlui
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor (id):
    if request.method=='GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de id{} não exite'.format(id)
            response = {'Status:': 'Erro', 'Mensagem:': mensagem }
        except Exception:
            mensagem = 'Erro desconhecido. Procure o ADMIN'
        return jsonify(response)
    elif request.method=='PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method=='DELETE':
        desenvolvedores.pop(id)
        return jsonif({'status': 'sucesso', 'mensagem': 'Registro excluido'})


#Lista todos os desenvolvedores e inclui um novo
@app.route('/dev/', methods= ['GET', 'POST'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    elif request.method == 'GET':
        return jsonify(desenvolvedores)

if __name__ == '__main__':
    app.run(debug=True)