import requests
from bs4 import BeautifulSoup
import time
from typing import Dict, Optional
import random
import os

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'

HEADERS = {
    'User-Agent': USER_AGENT,
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
}

# Toggle demo mode here or via environment variable
DEMO_MODE = os.getenv("DEMO_MODE", "False").lower() in ("1", "true", "yes")

def get_demo_data(platform: str, product_name: str) -> Dict:
    product_lower = product_name.lower()
    
    demo_prices = {
        'milk': {'Zepto': 65, 'Blinkit': 68, 'BigBasket': 62, 'JioMart': 64, 'Swiggy Instamart': 67},
        'bread': {'Zepto': 35, 'Blinkit': 32, 'BigBasket': 30, 'JioMart': 33, 'Swiggy Instamart': 34},
        'maggi': {'Zepto': 120, 'Blinkit': 115, 'BigBasket': 118, 'JioMart': 122, 'Swiggy Instamart': 119},
        'butter': {'Zepto': 55, 'Blinkit': 52, 'BigBasket': 50, 'JioMart': 54, 'Swiggy Instamart': 53},
        'rice': {'Zepto': 180, 'Blinkit': 175, 'BigBasket': 170, 'JioMart': 178, 'Swiggy Instamart': 182},
    }
    
    for key, prices in demo_prices.items():
        if key in product_lower:
            if random.random() < 0.85:
                return {
                    'platform': platform,
                    'price': f'₹{prices[platform]}',
                    'product_name': product_name.title(),
                    'available': True,
                    'url': f'https://demo-{platform.lower().replace(" ", "-")}.com/search?q={product_name}',
                    'demo': True
                }
    
    base_price = random.randint(50, 200)
    variation = random.randint(-15, 15)
    final_price = base_price + variation
    
    if random.random() < 0.75:
        return {
            'platform': platform,
            'price': f'₹{final_price}',
            'product_name': product_name.title(),
            'available': True,
            'url': f'https://demo-{platform.lower().replace(" ", "-")}.com/search?q={product_name}',
            'demo': True
        }
    else:
        return {
            'platform': platform,
            'price': 'N/A',
            'product_name': product_name,
            'available': False,
            'error': 'Platform blocking scraping (requires location/cookies)',
            'url': '',
            'demo': True
        }

def scrape_zepto(product_name: str) -> Dict:
    if DEMO_MODE:
        return get_demo_data('Zepto', product_name)
    
    try:
        search_url = f"https://www.zeptonow.com/search?query={product_name.replace(' ', '%20')}"
        response = requests.get(search_url, headers=HEADERS, timeout=10)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')
            
            price_element = soup.find('span', class_='price') or soup.find('div', class_='price')
            product_title = soup.find('h3') or soup.find('div', class_='product-name')
            
            if price_element:
                price_text = price_element.get_text(strip=True)
                return {
                    'platform': 'Zepto',
                    'price': price_text,
                    'product_name': product_title.get_text(strip=True) if product_title else product_name,
                    'available': True,
                    'url': search_url
                }
        
        return {
            'platform': 'Zepto',
            'price': 'N/A',
            'product_name': product_name,
            'available': False,
            'error': 'Requires location selection & anti-bot verification',
            'url': search_url
        }
    except Exception as e:
        return {
            'platform': 'Zepto',
            'price': 'N/A',
            'product_name': product_name,
            'available': False,
            'error': f'Connection error: Platform requires JavaScript/cookies',
            'url': ''
        }

def scrape_blinkit(product_name: str) -> Dict:
    if DEMO_MODE:
        return get_demo_data('Blinkit', product_name)
    
    try:
        search_url = f"https://blinkit.com/s/?q={product_name.replace(' ', '%20')}"
        response = requests.get(search_url, headers=HEADERS, timeout=10)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')
            
            price_element = soup.find('div', class_='Price__UpdatedPrice') or soup.find('span', text=lambda t: t and '₹' in str(t))
            product_title = soup.find('div', class_='Product__UpdatedTitle')
            
            if price_element:
                price_text = price_element.get_text(strip=True)
                return {
                    'platform': 'Blinkit',
                    'price': price_text,
                    'product_name': product_title.get_text(strip=True) if product_title else product_name,
                    'available': True,
                    'url': search_url
                }
        
        return {
            'platform': 'Blinkit',
            'price': 'N/A',
            'product_name': product_name,
            'available': False,
            'error': 'Requires location selection & anti-bot verification',
            'url': search_url
        }
    except Exception as e:
        return {
            'platform': 'Blinkit',
            'price': 'N/A',
            'product_name': product_name,
            'available': False,
            'error': f'Connection error: Platform requires JavaScript/cookies',
            'url': ''
        }

def scrape_bigbasket(product_name: str) -> Dict:
    if DEMO_MODE:
        return get_demo_data('BigBasket', product_name)
    
    try:
        search_url = f"https://www.bigbasket.com/ps/?q={product_name.replace(' ', '%20')}"
        response = requests.get(search_url, headers=HEADERS, timeout=10)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')
            
            price_element = soup.find('span', class_='Pricing___StyledLabel') or soup.find('span', text=lambda t: t and '₹' in str(t))
            product_title = soup.find('h3', class_='___S1TitleDesktop')
            
            if price_element:
                price_text = price_element.get_text(strip=True)
                return {
                    'platform': 'BigBasket',
                    'price': price_text,
                    'product_name': product_title.get_text(strip=True) if product_title else product_name,
                    'available': True,
                    'url': search_url
                }
        
        return {
            'platform': 'BigBasket',
            'price': 'N/A',
            'product_name': product_name,
            'available': False,
            'error': 'Requires location selection & anti-bot verification',
            'url': search_url
        }
    except Exception as e:
        return {
            'platform': 'BigBasket',
            'price': 'N/A',
            'product_name': product_name,
            'available': False,
            'error': f'Connection error: Platform requires JavaScript/cookies',
            'url': ''
        }

def scrape_jiomart(product_name: str) -> Dict:
    if DEMO_MODE:
        return get_demo_data('JioMart', product_name)
    
    try:
        search_url = f"https://www.jiomart.com/search/{product_name.replace(' ', '%20')}"
        response = requests.get(search_url, headers=HEADERS, timeout=10)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')
            
            price_element = soup.find('span', class_='jm-heading-xxs') or soup.find('span', text=lambda t: t and '₹' in str(t))
            product_title = soup.find('div', class_='jm-body-xs')
            
            if price_element:
                price_text = price_element.get_text(strip=True)
                return {
                    'platform': 'JioMart',
                    'price': price_text,
                    'product_name': product_title.get_text(strip=True) if product_title else product_name,
                    'available': True,
                    'url': search_url
                }
        
        return {
            'platform': 'JioMart',
            'price': 'N/A',
            'product_name': product_name,
            'available': False,
            'error': 'Requires location selection & anti-bot verification',
            'url': search_url
        }
    except Exception as e:
        return {
            'platform': 'JioMart',
            'price': 'N/A',
            'product_name': product_name,
            'available': False,
            'error': f'Connection error: Platform requires JavaScript/cookies',
            'url': ''
        }

def scrape_swiggy_instamart(product_name: str) -> Dict:
    if DEMO_MODE:
        return get_demo_data('Swiggy Instamart', product_name)
    
    try:
        search_url = f"https://www.swiggy.com/instamart/search?query={product_name.replace(' ', '%20')}"
        response = requests.get(search_url, headers=HEADERS, timeout=10)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')
            
            price_element = soup.find('div', class_='ProductCard_price') or soup.find('span', text=lambda t: t and '₹' in str(t))
            product_title = soup.find('div', class_='ProductCard_name')
            
            if price_element:
                price_text = price_element.get_text(strip=True)
                return {
                    'platform': 'Swiggy Instamart',
                    'price': price_text,
                    'product_name': product_title.get_text(strip=True) if product_title else product_name,
                    'available': True,
                    'url': search_url
                }
        
        return {
            'platform': 'Swiggy Instamart',
            'price': 'N/A',
            'product_name': product_name,
            'available': False,
            'error': 'Requires location selection & anti-bot verification',
            'url': search_url
        }
    except Exception as e:
        return {
            'platform': 'Swiggy Instamart',
            'price': 'N/A',
            'product_name': product_name,
            'available': False,
            'error': f'Connection error: Platform requires JavaScript/cookies',
            'url': ''
        }

# --- New function: get_prices_api ---
def _normalize_price_str(price_raw: Optional[str]) -> Optional[str]:
    if not price_raw:
        return None
    s = str(price_raw).strip()
    # If price is numeric or contains currency symbol keep as-is (trim extra words)
    # e.g. "₹ 65", "65.00", "INR 65"
    # Return trimmed string
    return s

def get_prices_api(product: str) -> Dict[str, Optional[str]]:
    """
    Try to fetch live prices via configured APIs. Returns a mapping {store_name: price_str}.
    Providers supported:
      - SerpAPI (preferred) when SERPAPI_API_KEY in env
      - RapidAPI-style provider when RAPIDAPI_HOST and RAPIDAPI_KEY in env (you must set endpoint specifics)
    If no API keys are present, returns empty dict.
    """
    product = product.strip()
    results: Dict[str, Optional[str]] = {}

    # 1) Try SerpAPI if configured
    serpapi_key = os.getenv("SERPAPI_API_KEY")
    if serpapi_key:
        try:
            params = {
                "engine": "google_shopping",
                "q": product,
                "google_domain": "google.co.in",
                "hl": "en",
                "gl": "in",
                "api_key": serpapi_key,
            }
            resp = requests.get("https://serpapi.com/search.json", params=params, timeout=10)
            if resp.status_code == 200:
                data = resp.json()
                shopping_results = data.get("shopping_results") or []
                # serpapi shopping_results: items with keys like title, source (merchant), price, price_raw
                for item in shopping_results:
                    source = item.get("source") or item.get("merchant") or item.get("store") or item.get("title") or "unknown"
                    price = item.get("price") or item.get("price_raw") or item.get("extracted_price")
                    if price:
                        results[source] = _normalize_price_str(price)
                # Map common names to our platforms (best-effort)
                mapped = {}
                platform_aliases = {
                    "Zepto": ["zepto"],
                    "Blinkit": ["blinkit", "grofers"],  # Grofers alias
                    "BigBasket": ["bigbasket", "big basket", "bbnow"],
                    "JioMart": ["jiomart", "jio mart"],
                    "Swiggy Instamart": ["swiggy", "instamart", "swiggy instamart"],
                }
                for plat, aliases in platform_aliases.items():
                    for k, v in results.items():
                        kl = k.lower()
                        if any(alias in kl for alias in aliases):
                            mapped[plat] = v
                            break
                # Also include any other stores found
                for k, v in results.items():
                    if k not in mapped.values():
                        # only include if not already mapped to an official platform
                        if k not in mapped:
                            mapped[k] = v
                return mapped
            else:
                # Non-200 from serpapi
                return {}
        except Exception:
            # Any error -> fallthrough to rapidapi or return empty
            pass

    # 2) Try RapidAPI (generic) if configured
    rapidapi_key = os.getenv("RAPIDAPI_KEY")
    rapidapi_host = os.getenv("RAPIDAPI_HOST")
    if rapidapi_key and rapidapi_host:
        try:
            # NOTE: You must set RAPIDAPI_HOST to the actual host your RapidAPI provider requires,
            # and the path below to the provider's endpoint. This is a template showing how to call.
            url = f"https://{rapidapi_host}/search"
            headers = {
                "X-RapidAPI-Key": rapidapi_key,
                "X-RapidAPI-Host": rapidapi_host,
                "Accept": "application/json"
            }
            params = {"q": product}
            resp = requests.get(url, headers=headers, params=params, timeout=10)
            if resp.status_code == 200:
                data = resp.json()
                # The parsing below is provider-specific. Adapt to the actual RapidAPI response schema.
                items = data.get("items") or data.get("results") or []
                for item in items:
                    source = item.get("store") or item.get("merchant") or item.get("source") or item.get("title")
                    price = item.get("price") or item.get("priceString") or item.get("displayPrice")
                    if source and price:
                        results[source] = _normalize_price_str(price)
                return results
            else:
                return {}
        except Exception:
            pass

    # No API credentials or nothing found
    return {}

def scrape_all_platforms(product_name: str) -> Dict:
    """
    Backwards-compatible wrapper that uses DEMO_MODE or falls back to per-platform scrapers.
    The front-end expects the shape: { 'query': product_name, 'platforms': [ {platform, price, ...}, ... ] }
    """
    results = {
        'query': product_name,
        'platforms': []
    }
    
    # If demo mode, use the existing per-platform demo scrapers
    if DEMO_MODE:
        scrapers = [
            scrape_zepto,
            scrape_blinkit,
            scrape_bigbasket,
            scrape_jiomart,
            scrape_swiggy_instamart
        ]
        for scraper in scrapers:
            result = scraper(product_name)
            results['platforms'].append(result)
            time.sleep(0.5)
    else:
        # Try to get prices via APIs first
        api_prices = get_prices_api(product_name)  # mapping store -> price_str
        # Known platforms we want to show in the UI
        known_platforms = [
            ('Zepto', f"https://www.zeptonow.com/search?query={product_name.replace(' ', '%20')}"),
            ('Blinkit', f"https://blinkit.com/s/?q={product_name.replace(' ', '%20')}"),
            ('BigBasket', f"https://www.bigbasket.com/ps/?q={product_name.replace(' ', '%20')}"),
            ('JioMart', f"https://www.jiomart.com/search/{product_name.replace(' ', '%20')}"),
            ('Swiggy Instamart', f"https://www.swiggy.com/instamart/search?query={product_name.replace(' ', '%20')}")
        ]
        for plat_name, plat_url in known_platforms:
            price_val = None
            # try direct match from API keys
            for k, v in api_prices.items():
                if k and plat_name.lower().split()[0] in k.lower():
                    price_val = v
                    break
            # fallback: sometimes API keys use slightly different names
            if not price_val:
                # exact key
                if plat_name in api_prices:
                    price_val = api_prices[plat_name]
            entry = {
                'platform': plat_name,
                'price': price_val if price_val else 'N/A',
                'product_name': product_name,
                'available': bool(price_val),
                'url': plat_url
            }
            results['platforms'].append(entry)
            # small delay to be polite (though APIs shouldn't require this)
            time.sleep(0.1)
    
    # Compute is_best_deal like original logic
    available_prices = [p for p in results['platforms'] if p.get('available') and p.get('price') != 'N/A']
    
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
                for p in results['platforms']:
                    p['is_best_deal'] = (p['platform'] == best_deal[0]['platform'])
            else:
                for p in results['platforms']:
                    p['is_best_deal'] = False
        except Exception:
            for p in results['platforms']:
                p['is_best_deal'] = False
    else:
        for p in results['platforms']:
            p['is_best_deal'] = False
    
    return results
