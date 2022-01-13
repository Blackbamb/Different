from flask import Flask
from flask import request

def mock_server():
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return 'Hello, World!!!!!!'

    @app.route('/plugin/diagnostic', methods=['GET', 'POST', 'DELETE'])
    def mock():
        if request.method == 'POST':
            return """{"status":"OK"}"""

    @app.route('/plugin/register', methods=['GET', 'POST', 'DELETE'])
    def mock1():
        if request.method == 'POST':
            return """{"status":"OK"}"""

    @app.route('/plugin', methods=['GET', 'POST', 'DELETE'])
    def mock2():
        if request.method == 'POST':
            return """{"status":"OK"}"""
    app.run()
mock_server()