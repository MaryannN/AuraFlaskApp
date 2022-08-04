# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request

# -- Initialization section --
app = Flask(__name__)

# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/results', methods=['GET', 'POST'])
def results():
  user_input = request.form
  return render_template('results.html', user_input=user_input)

app.run(host='0.0.0.0', port=81, debug=True)