from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# Rota principal
@app.route('/')
def index():
    return render_template('index.html')

# Rota para obter os dados da API JSON Placeholder
@app.route('/get_data')
def get_data():
    api_url_user = 'http://127.0.0.1:8000/user/'  # Altere para sua URL da API
    response_user = requests.get(api_url_user)
    data_user = response_user.json()
    return jsonify(data_user)

if __name__ == '__main__':
    app.run(debug=True)
