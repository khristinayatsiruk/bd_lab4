from flask import Flask, jsonify
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route("/api/hello", methods=["GET"])
def hello():
    """
    Hello endpoint.
    ---
    responses:
      200:
        description: Returns a greeting
        examples:
          application/json: {"message": "Hello, world!"}
    """
    return jsonify({"message": "Hello, world!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
