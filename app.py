from flask import Flask, render_template
from datetime import datetime

##app se chama app pq é uma convenção
##que argumento eu passo pro flask? O nome da aplicação
app = Flask("hello")
posts = [
    {
        "title": "First post",
        "body": "Post content",
        "author": "Vinicius",
        "created": datetime(2022, 7, 25)
    },
    {
        "title": "Second post",
        "body": "Post content",
        "author": "Jubileu",
        "created": datetime(2022, 7, 26)
    }
]


##estou criando minha primeira rota
@app.route("/")
@app.route("/hello")
##CRIA UMA FUNÇÃO QUE RETORNA HELLO WORLD
def hello():
    return "Hello World"

@app.route("/meucontato")
def meuContato():
    return render_template('index.html')

@app.route("/")
def index():
    return render_template('index.html', 
                            posts=posts
                            )

@app.route("/login")
def login():
    return render_template('login.html')