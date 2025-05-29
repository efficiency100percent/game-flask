from flask import Flask,render_template

app = Flask(__name__) # initiate flask

# rendered all htmls pages in decorator
@app.route('/')
def hello_world():
  return render_template("index.html")

@app.route('/cert')
def certification():
  return render_template("cert.html")

@app.route('/edu')
def education():
  return render_template("edu.html")

@app.route('/exp')
def experience():
  return render_template("exp.html")

@app.route('/portfolio')
def portfolio():
  return render_template("portfolio.html")

@app.route('/game')
def game():
  return render_template("game.html")

@app.route('/article')
def article():
  return render_template("article.html")

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
