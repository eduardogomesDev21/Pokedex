from flask import Flask, jsonify, send_file
import requests

app = Flask(__name__)

# Rota principal para servir o HTML (Frontend)
@app.route('/')
def home():
    return send_file('interface.html')

# Rota da API (Backend) para consultar os dados do Pokémon
@app.route('/api/pokemon/<id_or_name>')
def get_pokemon(id_or_name):
    # O backend faz a comunicação com a API externa e devolve pro frontend
    url = f"https://pokeapi.co/api/v2/pokemon/{id_or_name.lower().strip()}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({'error': 'Pokémon não encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("Iniciando a Pokédex...")
    print("Acesse no navegador: http://127.0.0.1:5000/")
    app.run(debug=True)
