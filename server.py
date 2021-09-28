from flask import Flask, render_template, session, redirect
import random

from flask.globals import request

app = Flask (__name__)
app.secret_key = 'secret2021'

@app.route('/', methods=['GET'])
def index():
    number = random.randint(1, 100)
    if 'number' not in session:
        session['number'] = number
    print (number)
    print (session['number'])
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    session['guess'] = int(request.form['guess'])
    # print(request.form)
    print(session['guess'])
    if 'attempts' not in session:
        session['attempts'] = 0
    session['attempts'] = int(session['attempts']) + 1
    print(session['attempts'])
    return redirect('/')

@app.route('/restart', methods=['POST'])
def restart():
    session.pop('number')
    session.pop('guess')
    session.pop('attempts')
    return redirect('/')

if __name__ == ('__main__'):
    app.run(debug=True)