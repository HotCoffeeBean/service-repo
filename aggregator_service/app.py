from flask import Flask, jsonify
import requests

app = Flask(__name__)
#from flask_cors import CORS
#CORS(app)

RESPONSE_SERVICE_URL = "http://response-service:5000/responses"

@app.route('/results', methods=['GET'])
def aggregate():
    res = requests.get(RESPONSE_SERVICE_URL)
    data = res.json()

    result = {}

    for response in data:
        survey_id = response.get("survey_id")
        answer = response.get("answer")

        if survey_id not in result:
            result[survey_id] = {}

        if answer not in result[survey_id]:
            result[survey_id][answer] = 0

        result[survey_id][answer] += 1

    return jsonify(result)

if __name__ == "__main__":
    app.run(host='0.0.0.0')