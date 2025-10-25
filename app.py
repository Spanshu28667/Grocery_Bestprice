from flask import Flask, render_template, request, jsonify
from scrapers import scrape_all_platforms
import os

app = Flask(__name__)
app.secret_key = os.getenv('SESSION_SECRET', 'dev-secret-key-change-in-production')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    product_name = request.json.get('product_name', '').strip()
    
    if not product_name:
        return jsonify({'error': 'Please enter a product name'}), 400
    
    results = scrape_all_platforms(product_name)
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
