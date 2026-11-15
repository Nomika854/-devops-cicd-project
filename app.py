
from flask import Flask, request, jsonify

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return "Welcome to DevOps CI/CD Calculator Application!"

# Calculator operations
@app.route("/calculate")
def calculate():
    try:
        a = float(request.args.get("a", 0))
        b = float(request.args.get("b", 0))
        operation = request.args.get("operation", "add")

        if operation == "add":
            result = a + b

        elif operation == "subtract":
            result = a - b

        elif operation == "multiply":
            result = a * b

        elif operation == "divide":
            if b == 0:
                return jsonify({"error": "Division by zero"}), 400
            result = a / b

        else:
            return jsonify({"error": "Invalid operation"}), 400

        return jsonify({"result": result})

    except ValueError:
        return jsonify({"error": "Invalid input"}), 400

# Application health check
@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200


if __name__ == "__main__":
    app.run(debug=False)
