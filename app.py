# -*- coding: utf-8 -*-

import json
import base64

from flask import Flask, request, jsonify, render_template


app = Flask(__name__)

def check_best_bus_placement(input):
    return {
        "stelplaats": "De Lijn Arsenaal",
        "parking": [],
        "garage": {
            "groot": [
                {"bus": "1000",type: "GROOT"},
                {"bus": "1001",type: "GROOT"},
                {"bus": "1002",type: "GROOT"},
                {"bus": "2000",type: "NORMAAL"},
                {"bus": "2001",type: "NORMAAL"}
            ],
            "medium": [
                {"bus": "2002",type: "NORMAAL"},
                {"bus": "2003",type: "NORMAAL"},
                {"bus": "2004",type: "NORMAAL"},
                {"bus": "2005",type: "NORMAAL"},
                {"bus": "3000",type: "MINI"},
                {"bus": "3001",type: "MINI"},
                {"bus": "3002",type: "MINI"},
                {"bus": "3003",type: "MINI"}		
            ],
            "klein": [
                {"bus": "3004",type: "MINI"},
                {"bus": "3005",type: "MINI"},
                {"bus": "3006",type: "MINI"},
                {"bus": "3007",type: "MINI"},
                {"bus": "3008",type: "MINI"},
                {"bus": "3009",type: "MINI"},
                {"bus": "3010",type: "MINI"},
                {"bus": "3011",type: "MINI"},
                {"bus": "3012",type: "MINI"}		
            ]
        }
    }

@app.route('/parking', methods=['POST'])
def parking():
    try:
        files = request.files
        json_stringed = files['inputdata'].read()
        jsoned = json.loads(json_stringed.decode('utf-8'))
        result = check_best_bus_placement(jsoned)
        return jsonify({'status': 'success', 'message': result})
    except Exception as e:
        return jsonify({'status': 'error', 'message': e})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)