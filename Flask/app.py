from flask import Flask, render_template, request
import joblib
import numpy as np
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = joblib.load(os.path.join(BASE_DIR, "model.pkl"))
scaler = joblib.load(os.path.join(BASE_DIR, "scaler.pkl"))

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/predict")
def predict():
    return render_template("predict.html")


@app.route("/result", methods=["POST"])
def result():
    try:
        gender = int(request.form["gender"])
        married = int(request.form["married"])
        dependents = int(request.form["dependents"])
        education = int(request.form["education"])
        self_employed = int(request.form["self_employed"])
        applicant_income = float(request.form["applicant_income"])
        coapplicant_income = float(request.form["coapplicant_income"])
        loan_amount = float(request.form["loan_amount"])
        loan_term = float(request.form["loan_term"])
        credit_history = float(request.form["credit_history"])
        property_area = int(request.form["property_area"])

        features = np.array([[
            gender,
            married,
            dependents,
            education,
            self_employed,
            applicant_income,
            coapplicant_income,
            loan_amount,
            loan_term,
            credit_history,
            property_area
        ]])

        features = scaler.transform(features)

        prediction = model.predict(features)[0]

        if prediction == 1:
            status = "Loan Approved "
            color = "green"
        else:
            status = "Loan Rejected "
            color = "red"

        return render_template(
            "result.html",
            prediction=status,
            color=color
        )

    except Exception as e:
        return f"Error : {e}"


if __name__ == "__main__":
    app.run(debug=True)     