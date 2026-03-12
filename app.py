from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# conexão com banco
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sistema_clientes"
)

# abrir tela de produtos
@app.route('/')
def produtos():
    return render_template('produtos.html')


# abrir tela de cadastro
@app.route('/cadastro/<produto>')
def cadastro(produto):
    return render_template('index.html', produto=produto)


# salvar cliente no banco
@app.route('/salvar', methods=['POST'])
def salvar():

    nome = request.form['nome']
    email = request.form['email']
    telefone = request.form['telefone']
    produto = request.form['produto']

    cursor = conexao.cursor()

    sql = "INSERT INTO clientes (nome,email,telefone,produto) VALUES (%s,%s,%s,%s)"
    valores = (nome,email,telefone,produto)

    cursor.execute(sql,valores)

    conexao.commit()

    return "Cliente salvo com sucesso!"


if __name__ == '__main__':
    app.run(debug=True)