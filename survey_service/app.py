from flask import Flask, request, jsonify

app = Flask(__name__)
#from flask_cors import CORS
#CORS(app)

surveys = []

@app.route('/survey', methods=['POST'])
def create_survey():
    data = request.json
    surveys.append(data)
    return jsonify({"msg": "Survey created"}), 201

@app.route('/survey', methods=['GET'])
def get_surveys():
    return jsonify(surveys)

@app.route('/survey/<int:id>', methods=['DELETE'])
def delete_survey(id):
    if id < len(surveys):
        surveys.pop(id)
        return jsonify({"msg": "Deleted"})
    return jsonify({"msg": "Not found"}), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0')