from flask import Flask, render_template

##app se chama app pq é uma convenção
##que argumento eu passo pro flask? O nome da aplicação
app = Flask("hello")

##estou criando minha primeira rota
@app.route("/")
@app.route("/hello")
##CRIA UMA FUNÇÃO QUE RETORNA HELLO WORLD
def hello():
    return "Hello World"

@app.route("/meucontato")
def meuContato():
    return render_template('index.html')

