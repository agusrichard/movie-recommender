from flask import Flask, jsonify, request
from .recommender import recommender

app = Flask(__name__)
get_recommendations = recommender()

@app.route('/', methods=['GET'])
def index():
    return jsonify({
        'success': True,
        'message': 'We did it!'
    })

@app.route('/recommendations', methods=['GET', 'POST'])
def recommend():
    data = request.get_json()
    result = get_recommendations(data['title'], int(data['number']))
    if type(result) == list and not result:
        return jsonify({
            'success': False,
            'message': f"No movies with title {data['title']}"
        })
    return jsonify({
        'success': True,
        'message': 'Success to get movie recommendations',
        'data': result.tolist()
    })

if __name__ == '__main__':
    app.run(debug=True)
