from flask import Flask, request, jsonify
from geo import *

app = Flask(__name__)

@app.route('/circulo',methods=['POST'])
def circulo():
    try:
        data = request.get_json()
        radio = data['radio']
        resArea = areaCirculo(radio)
        return jsonify({'area':resArea})
    except Exception as e:
        return jsonify({'error':str(e)}),400
if __name__ == '__main__':
    app.run(debug=False, port=5001)