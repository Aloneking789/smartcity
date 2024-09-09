from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/report_issue', methods=['POST'])
def report_issue():
    issue = request.json
    # Logic to store issue in the database
    print("Issue reported:", issue)
    return jsonify({"status": "Issue reported successfully"}), 200

@app.route('/api/issues', methods=['GET'])
def get_issues():
    # Example static issue list, in practice you'd fetch this from a DB
    issues = [
        {"id": 1, "type": "Pothole", "location": "Location A"},
        {"id": 2, "type": "Barricade", "location": "Location B"}
    ]
    return jsonify(issues)

if __name__ == '__main__':
    app.run(debug=True)
