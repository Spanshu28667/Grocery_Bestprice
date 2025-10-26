from flask import Flask, request, jsonify, render_template
import scrapers
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Render your existing UI (assumes templates/index.html exists)
    return render_template('index.html')

@app.route('/search')
def search():
    """
    Query parameter: ?q=product name
    Behavior:
      - If scrapers.DEMO_MODE is True, uses existing demo scrapers (scrape_all_platforms).
      - If scrapers.DEMO_MODE is False, uses scrapers.get_prices_api to fetch live prices,
        builds the same JSON shape as scrape_all_platforms, and returns it.
    """
    product = request.args.get('q', '').strip()
    if not product:
        return jsonify({"error": "Missing product query parameter 'q'"}), 400

    # If demo mode, keep existing behavior
    if scrapers.DEMO_MODE:
        results = scrapers.scrape_all_platforms(product)
        return jsonify(results)

    # Live mode: use API prices and keep the same output shape
    api_prices = scrapers.get_prices_api(product)  # mapping store -> price_str
    known_platforms = [
        ('Zepto', f"https://www.zeptonow.com/search?query={product.replace(' ', '%20')}"),
        ('Blinkit', f"https://blinkit.com/s/?q={product.replace(' ', '%20')}"),
        ('BigBasket', f"https://www.bigbasket.com/ps/?q={product.replace(' ', '%20')}"),
        ('JioMart', f"https://www.jiomart.com/search/{product.replace(' ', '%20')}"),
        ('Swiggy Instamart', f"https://www.swiggy.com/instamart/search?query={product.replace(' ', '%20')}")
    ]

    platforms = []
    for plat_name, plat_url in known_platforms:
        # Find a matching key (best-effort)
        price_val = None
        for k, v in api_prices.items():
            if k and plat_name.lower().split()[0] in k.lower():
                price_val = v
                break
        if not price_val and plat_name in api_prices:
            price_val = api_prices[plat_name]

        entry = {
            'platform': plat_name,
            'price': price_val if price_val else 'N/A',
            'product_name': product,
            'available': bool(price_val),
            'url': plat_url
        }
        platforms.append(entry)

    # compute is_best_deal
    available_prices = [p for p in platforms if p['available'] and p['price'] != 'N/A']
    if available_prices:
        try:
            prices_with_values = []
            for p in available_prices:
                price_str = str(p['price']).replace('₹', '').replace(',', '').strip()
                try:
                    price_value = float(price_str.split()[0])
                    prices_with_values.append((p, price_value))
                except (ValueError, IndexError):
                    pass
            if prices_with_values:
                best_deal = min(prices_with_values, key=lambda x: x[1])
                for p in platforms:
                    p['is_best_deal'] = (p['platform'] == best_deal[0]['platform'])
            else:
                for p in platforms:
                    p['is_best_deal'] = False
        except Exception:
            for p in platforms:
                p['is_best_deal'] = False
    else:
        for p in platforms:
            p['is_best_deal'] = False

    result = {
        'query': product,
        'platforms': platforms
    }
    return jsonify(result)

if __name__ == '__main__':
    # Use PORT env var for Render deployment
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
