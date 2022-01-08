from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/')
def index():
    response = {'ok':True, 'data':[], 'message' : 'Api is on!'}
    return json.dumps(response)

if __name__ == "__main__":
    app.run(debug=True)