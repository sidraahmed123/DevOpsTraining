import flask
app = flask.Flask(__name__, template_folder="./") 

bus_stop_arrivals = [
    {'bus stop name': 'Pimlico D', 'time': '12.00', 'bus number': 'P16'},
    {'bus stop name': 'Pimlico E', 'time': '13.00', 'bus number': 'P15'} 
]

@app.route('/hello_world')
def hello_world():
    return flask.render_template('index.html')
   




