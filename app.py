import json
from flask import Flask, request, render_template
from flask_cors import CORS
from pytest import raises
import shortuuid

app = Flask(__name__)
CORS(app)

submissions = {}

# NOTE: This route is needed for the default EB health check route
@app.route('/')  
def home():
    return render_template("marquee/index.html")

@app.route('/assignment', methods=["POST"])
def post_assignment():
    payload = json.loads(request.data)
    uuid = shortuuid.uuid()
    submissions[uuid] = payload
    return {"id": uuid}

@app.route('/assignment/<id>', methods=["GET"])
def get_assignment(id):
    return submissions[id]

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)
    


# def test_float():
#     with raises(TypeError):  # Assert the code block raises an exception.
#         assert is_even(4.5)