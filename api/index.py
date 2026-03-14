from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Sistema funcionando no Vercel 🚀"

# isto é obrigatório para o Vercel
app = app