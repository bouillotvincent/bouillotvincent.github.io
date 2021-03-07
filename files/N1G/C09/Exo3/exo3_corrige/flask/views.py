from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route('/')
def index():
  date = datetime.datetime.now()
  h = date.hour
  m = date.minute
  s = date.second
  return render_template("index.html", heure = h, minute = m, seconde = s)

@app.route('/resultat',methods = ['POST'])
def resultat():
  result = request.form
  n = result['nom']
  p = result['prenom']
  return render_template("resultat.html", nom=n, prenom=p)

'''
@app.route('/resultat',methods = ['GET'])
def resultat():
  result=request.args
  n = result['nom']
  p = result['prenom']
  return render_template("resultat.html", nom=n, prenom=p)
'''

@app.route('/about')
def about():
    return "<p> Une autre page est possible </p>"
app.run(debug=True)
