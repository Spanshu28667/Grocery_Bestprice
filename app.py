from flask import Flask, request, jsonify, render_template
import scrapers
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Your UI page

@app.route('/search')
def search():
    """
    Query: ?q=product_name
    Returns JSON with platforms and prices.
    Supports DEMO_MODE or live API.
    """
    product = request.args.get('q', '').strip()
    if not product:
        return jsonify({"error": "Missing product query parameter 'q'"}), 400

    if scrapers.DEMO_MODE:
        results = scrapers.scrape_all_platforms(product)
        return jsonify(results)

    # Live API mode
    api_prices = scrapers.get_prices_api(product)  # {platform: price}
    known_platforms = [
        ('Zepto', f"https://www.zeptonow.com/search?query={product.replace(' ', '%20')}"),
        ('Blinkit', f"https://blinkit.com/s/?q={product.replace(' ', '%20')}"),
        ('BigBasket', f"https://www.bigbasket.com/ps/?q={product.replace(' ', '%20')}"),
        ('JioMart', f"https://www.jiomart.com/search/{product.replace(' ', '%20')}"),
        ('Swiggy Instamart', f"https://www.swiggy.com/instamart/search?query={product.replace(' ', '%20')}")
    ]

    platforms = []
    for plat_name, plat_url in known_platforms:
        price_val = api_prices.get(plat_name, 'N/A')
        platforms.append({
            'platform': plat_name,
            'price': price_val,
            'product_name': product,
            'available': price_val != 'N/A',
            'url': plat_url
        })

    # Determine best deal
    available_prices = [p for p in platforms if p['available'] and p['price'] != 'N/A']
    if available_prices:
        try:
            prices_with_values = []
            for p in available_prices:
                price_str = str(p['price']).replace('₹','').replace(',','').strip()
                price_val = float(price_str.split()[0])
                prices_with_values.append((p, price_val))
            best_deal = min(prices_with_values, key=lambda x: x[1])
            for p in platforms:
                p['is_best_deal'] = (p['platform'] == best_deal[0]['platform'])
        except:
            for p in platforms:
                p['is_best_deal'] = False
    else:
        for p in platforms:
            p['is_best_deal'] = False

    return jsonify({
        'query': product,
        'platforms': platforms
    })

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
