# -*- coding: utf-8 -*-

import json
import base64
import algorithm

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


def check_best_bus_placement(input_):
    return algorithm.assign_busses(input_)


@app.route('/parking', methods=['POST'])
def parking():
    try:
        files = request.files
        json_stringed = files['jsoninput'].read()
        jsoned = json.loads(json_stringed.decode('utf-8'))
        result = check_best_bus_placement(jsoned)
        print('RESULT : ', result)
        return jsonify({'status': 'success', 'message': result})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
