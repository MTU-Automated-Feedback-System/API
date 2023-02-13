from flask import Flask, render_template
from flask_cors import CORS
from services import assignment, submission

app = Flask(__name__)
CORS(app)

# Apply blueprints to the app
app.register_blueprint(assignment.bp)
app.register_blueprint(submission.bp)

# NOTE: This route is needed for the default EB health check route
@app.route('/')  
def home():
    return render_template("marquee/index.html")

