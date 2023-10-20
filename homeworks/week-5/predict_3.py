import pickle


with open("model1.bin", "rb") as f_mv:
    model = pickle.load(f_mv)

with open("dv.bin", "rb") as f_dv:
    dv = pickle.load(f_dv)

client = {"job": "retired", "duration": 445, "poutcome": "success"}

X = dv.transform([client])
y_pred = model.predict_proba(X)[0, 1]

print("Probability of client getthing card is",y_pred)