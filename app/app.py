from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return jsonify({
        'success': True,
        'message': 'We did it!'
    })

@app.route()

if __name__ == '__main__':
    app.run(debug=True)
