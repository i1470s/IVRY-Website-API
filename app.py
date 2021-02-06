import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

endpoints = [    
    {'id': 0,
     'name': 'structure'},
    {'id': 1,
     'name': 'rss'},
    {'id': 2,
     'name': 'COMING SOON'},
    {'id': 3,
     'name': 'COMING SOON'},
    {'id': 4,
     'name': 'COMING SOON'},
    {'id': 5,
     'name': 'COMING SOON'},
    {'id': 6,
     'name': 'COMING SOON'},
    {'id': 7,
     'name': 'COMING SOON'},
    {'id': 8,
     'name': 'COMING SOON'},
    {'id': 9,
     'name': 'COMING SOON'},]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>IVRY API V1</h1>
            <h2>Welcome</h2>
            <br>
            <h3>API Endpoints<h3>
            <p>https://api-ivry.tk/api/v1/</p>
            <br>
            <h3>Our Website<h3>
            <p>https://ivry.tk/</p>'''

@app.route('/api/v1/', methods=['GET'])
def api():
    return jsonify(endpoints)

@app.route('/api/v1/structure', methods=['GET'])
def structure():
    return '''  
├── https://api-ivry.tk/ <br>
⠀└── /api/v1/ <br>
⠀⠀└── structure <br>
⠀⠀└── rss <br>''' 


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

app.run()