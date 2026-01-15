from flask import Flask, request, jsonify
import requests
import re

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>Reddit JSON Proxy</h1>
    <p>Usage: Pass a Reddit URL as the <code>url</code> query parameter.</p>
    <p>Example: <code>/?url=https://www.reddit.com/r/AZURE/comments/1g0mkwi/title_unexpected_50k_azure_bill_for_openai</code></p>
    '''

@app.route('/fetch')
def fetch_reddit():
    url = request.args.get('url')
    
    if not url:
        return jsonify({'error': 'Missing url parameter'}), 400
    
    # Validate it's a Reddit URL
    if not re.match(r'^https?://(www\.)?reddit\.com/', url):
        return jsonify({'error': 'Not a valid Reddit URL'}), 400
    
    # Remove trailing slash if present
    url = url.rstrip('/')
    
    # Remove .json if already present (to avoid .json.json)
    if url.endswith('.json'):
        url = url[:-5]
    
    # Append .json
    json_url = url + '.json'
    
    try:
        resp = requests.get(
            json_url,
            headers={
                'User-Agent': 'RedditProxy/1.0 (Educational Purpose)'
            },
            timeout=10
        )
        resp.raise_for_status()
        return jsonify(resp.json())
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
