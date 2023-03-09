from flask import Flask, render_template
from flask_cors import CORS
from services import exercise, submission

app = Flask(__name__)
CORS(app)

# Apply blueprints to the app
app.register_blueprint(exercise.bp)
app.register_blueprint(submission.bp)

# NOTE: This route is needed for the default EB health check route
@app.route('/')  
def home():
    return render_template("marquee/index.html")

