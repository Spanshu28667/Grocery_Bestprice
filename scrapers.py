import requests
from bs4 import BeautifulSoup
import time
from typing import Dict, Optional
import random

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'

HEADERS = {
    'User-Agent': USER_AGENT,
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
}

DEMO_MODE = True

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

def scrape_all_platforms(product_name: str) -> Dict:
    results = {
        'query': product_name,
        'platforms': []
    }
    
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
    
    available_prices = [p for p in results['platforms'] if p['available'] and p['price'] != 'N/A']
    
    if available_prices:
        try:
            prices_with_values = []
            for p in available_prices:
                price_str = p['price'].replace('₹', '').replace(',', '').strip()
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
