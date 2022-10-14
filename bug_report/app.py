from flask import (Flask,render_template)

from bug_report.api import api_blueprint

app = Flask(__name__)
app.register_blueprint(api_blueprint)

@app.get('/')
def index():
    return render_template('index.html')