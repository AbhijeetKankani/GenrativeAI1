import os
import subprocess
import sys

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/run_program', methods=['POST'])
def run_program():
    try:
        data = request.get_json()
        query = data['query']

        # Print the received query for debugging
        print("Received query:", query)

        # Execute your Python program
        output = subprocess.check_output([sys.executable, 'Chat.py', query])

        return jsonify({'output': output.decode()})
    except Exception as e:
        print("Error:", e)  # Print the exception for debugging
        # Return an error response with a 500 status code
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))  # Use port 8080 as default
    # Bind to all available network interfaces
    app.run(host='0.0.0.0', port=port)
