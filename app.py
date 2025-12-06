from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow frontend connection

# URL bridge
@app.route('/send', methods=['POST'])
def send():
    data = request.get_json()
    print("inputdata:", data)
    return jsonify({"Message": "message received success"})

if __name__ == '__main__':
    app.run(debug=True)
