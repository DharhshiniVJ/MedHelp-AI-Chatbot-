from flask import Flask, request, jsonify, render_template
from utils.rag_pipeline import get_department

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_department", methods=["POST"])
def department_lookup():
    data = request.get_json()
    symptoms = data.get("symptoms", "")

    if not symptoms:
        return jsonify({"error": "No symptoms provided"}), 400

    try:
        department = get_department(symptoms)
        return jsonify({"department": department})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
