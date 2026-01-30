from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# ---------- HTML ROUTES ----------

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/math", methods=["POST"])
def math_html():
    num1 = float(request.form["num1"])
    num2 = float(request.form["num2"])
    ops = request.form["operation"]

    if ops == "+":
        result = f"The sum of {num1} and {num2} is {num1 + num2}"
    elif ops == "-":
        result = f"The difference of {num1} and {num2} is {num1 - num2}"
    elif ops == "*":
        result = f"The product of {num1} and {num2} is {num1 * num2}"
    elif ops == "/":
        if num2 == 0:
            result = "Error: Division by zero"
        else:
            result = f"The division of {num1} by {num2} is {num1 / num2}"
    else:
        result = "Invalid operation"

    return render_template("result.html", result=result)


# ---------- POSTMAN / API ROUTE ----------

@app.route("/postman_action", methods=["POST"])
def math_postman():
    data = request.get_json()

    num1 = float(data["num1"])
    num2 = float(data["num2"])
    ops = data["operation"]

    if ops == "+":
        result = num1 + num2
    elif ops == "-":
        result = num1 - num2
    elif ops == "*":
        result = num1 * num2
    elif ops == "/":
        if num2 == 0:
            return jsonify({"error": "Division by zero"}), 400
        result = num1 / num2
    else:
        return jsonify({"error": "Invalid operation"}), 400

    return jsonify({
        "num1": num1,
        "num2": num2,
        "operation": ops,
        "result": result
    })


if __name__ == "__main__":
    app.run(debug=True)
