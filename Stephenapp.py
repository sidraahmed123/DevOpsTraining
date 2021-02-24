from flask import Flask, render_template
app = Flask(__name__)

@app.rpute('/')
def hello_world():
    return 'Hello World!'

@app.route('/world_domination_plans')
def world_domincation_plans(): 
    return 'thats a secert'

@app.route('/great/<name>')
def greet(name):
    return 'Hello, ' + name + '!'

@app.route('/html')
def html():
    return '<html><body><b>HTML!</b></body></html>'

@app.route('/betterhtml')
def betterhtml():
    return render_template(index.html)
