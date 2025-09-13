# Importa a biblioteca Flask
from flask import Flask

# Cria uma instância da aplicação
app = Flask(__name__)

# Define uma rota para a página inicial
@app.route('/')
def home():
    return "<h1>Olá, mundo! A sua aplicação está rodando no Docker.</h1>"

# Executa a aplicação quando o script é rodado
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)