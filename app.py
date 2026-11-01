from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/health')
def health_check():
    return jsonify({'status': 'healthy'}), 200

@app.route('/<username>')
def get_user_gists(username):
    url = f"https://api.github.com/users/{username}/gists"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return jsonify(data)

    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 401:
            return jsonify({'error': 'Unauthorized access'}), 401
        elif e.response.status_code == 404:
            return jsonify({'error': 'User not found'}), 404
        elif e.response.status_code == 403:
            return jsonify({'error': 'Rate limit exceeded'}), 403
        elif e.response.status_code == 500:
            return jsonify({'error': 'Internal server error'}), 500
        elif e.response.status_code == 503:
            return jsonify({'error': 'Service unavailable'}), 503
        else:
            return jsonify({'error': 'Unexpected error occurred'}), e.response.status_code

    except requests.exceptions.Timeout:
        return jsonify({'error': 'Request timed out'}), 504 

    except requests.exceptions.ConnectionError:
        return jsonify({'error': 'Connection failed — check your internet or the URL'}), 502

if __name__ == '__main__':
    app.run(debug=True)

