from flask import Flask, request, jsonify

app = Flask(__name__)
#from flask_cors import CORS
#CORS(app)

responses = []

@app.route('/response', methods=['POST'])
def submit_response():
    data = request.json
    responses.append(data)
    return jsonify({"msg": "Response saved"}), 201

@app.route('/responses', methods=['GET'])
def get_responses():
    return jsonify(responses)

if __name__ == "__main__":
    app.run(host='0.0.0.0')