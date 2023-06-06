from flask import Flask, jsonify, request

app = Flask(__name__)

frequencias = []
proximo_id = 1

# Rota para exibir a página inicial
@app.route('/index')
def index():
    reicionar_frequencia():
    global proximo_id

    disciplina = request.json.get('disciplina')
    aluno = request.json.get('aluno')
    data = request.json.get('data')
    presenca = request.json.get('presenca')

    nova_frequencia = {
        'id': proximo_id,
        'disciplina': disciplina,
        'aluno': aluno,
        'data': data,
        'presenca': presenca
    }

    frequencias.append(nova_frequencia)
    proximo_id += 1

    return jsonify(nova_frequencia), 201

# Rota para editar uma frequência existente
@app.route('/editar-frequencia/<int:id>', methods=['PUT'])
def editar_frequencia(id):
    frequencia = next((f for f in frequencias if f['id'] == id), None)
    if frequencia:
        frequencia['disciplina'] = request.json.get('disciplina')
        frequencia['aluno'] = request.json.get('aluno')
        frequencia['data'] = request.json.get('data')
        frequencia['presenca'] = request.json.get('presenca')
        return jsonify(frequencia)
    else:
        return jsonify({'message': 'Frequência não encontrada.'}), 404

# Rota para excluir uma frequência existente
@app.route('/excluir-frequencia/<int:id>', methods=['DELETE'])
def excluir_frequencia(id):
    global frequencias
    frequencias = [f for f in frequencias if f['id'] != id]
    return '', 204

if __name__ == '__main__':
    app.run()turn 'Bem-vindo ao Registro de Frequência!'

# Rota para ver todas as frequências registradas
@app.route('/ver-frequencia')
def ver_frequencia():
    return jsonify(frequencias)

# Rota para adicionar uma nova frequência
@app.route('/adicionar-frequencia', methods=['POST'])
def ad