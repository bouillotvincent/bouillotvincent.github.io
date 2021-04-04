from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return "<h1>Créer un site web côté serveur</h1> <p>Tout fonctionne parfaitement</p>"

@app.route('/about')
def about():
  return "<p>Une autre page est possible ! </p>"

app.run(debug=False)
