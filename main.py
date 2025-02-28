from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/app/<variable>')
def hello(variable):
    return jsonify({
        "message": f"Hello from Cloud Run! Variable: {variable}"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
