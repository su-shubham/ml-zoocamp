import pickle
from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

with open("model1.bin", "rb") as f_mv:
    model = pickle.load(f_mv)

with open("dv.bin", "rb") as f_dv:
    dv = pickle.load(f_dv)


@app.route("/risk", methods=["POST"])
def predict_client():
    client = request.get_json()
    X = dv.transform([client])
    y_pred = model.predict_proba(X)[0, 1]
    cred_risk = y_pred >= 0.5
    result = {"Risk Probaility": round(float(y_pred),3), "Good Credit": bool(cred_risk)}
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0",port=8080)