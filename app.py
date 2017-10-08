from flask import Flask, jsonify, request, abort
from sqlalchemy.sql.expression import func, text
from datetime import datetime
import logging

app = Flask(__name__)

PORT=8000

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify("hello world")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=PORT)
