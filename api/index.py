from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Sistema rodando no Vercel 🚀"

def handler(request):
    return app(request.environ, lambda status, headers: None)