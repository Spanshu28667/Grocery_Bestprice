# Grocery Price Comparison App

A Python-based web application that compares product prices across multiple grocery delivery platforms in India.

## Supported Platforms

- **Zepto**
- **Blinkit**
- **BigBasket**
- **JioMart**
- **Swiggy Instamart**

## Features

- 🔍 Search for any grocery product by name
- 💰 Compare prices across all 5 platforms simultaneously
- 🎯 Automatically highlights the best deal
- 🛡️ Graceful error handling for blocked or unavailable platforms
- 🌐 Simple web interface accessible through your browser
- 💻 Runs completely offline on your local machine

## Installation & Setup

### Prerequisites

- Python 3.11 or higher
- pip (Python package manager)

### Running on Replit

1. The app is already configured and ready to run
2. Click the "Run" button at the top
3. The app will open in the webview on port 5000

### Running Locally on Your Laptop

1. **Download the project files** from Replit (or clone if using git)

2. **Install Python** (if not already installed):
   - Windows: Download from [python.org](https://www.python.org/downloads/)
   - Mac: `brew install python3`
   - Linux: `sudo apt-get install python3 python3-pip`

3. **Navigate to the project folder**:
   ```bash
   cd path/to/grocery-price-comparison
   ```

4. **Install dependencies**:
   ```bash
   pip install flask requests beautifulsoup4 lxml selenium python-dotenv
   ```
   
   Or using the requirements file:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**:
   ```bash
   python app.py
   ```

6. **Open your browser** and go to:
   ```
   http://localhost:5000
   ```

## How to Use

1. Open the app in your browser
2. Enter a product name (e.g., "Amul milk 1L", "Maggi noodles", "Britannia bread")
3. Click "Search Prices"
4. View the price comparison table showing results from all platforms
5. The best deal will be highlighted in green

## Important Notes

⚠️ **Web Scraping Limitations**:
- Most of these platforms use anti-scraping measures and dynamic JavaScript rendering
- Some platforms may block automated requests
- The app handles these cases gracefully by showing "Not Available" status
- Results may be limited or unavailable depending on platform restrictions

🔒 **Privacy**:
- All operations run locally on your machine
- No data is sent to external servers
- No personal information is collected or stored

## Troubleshooting

### Python or pip not found

- **Windows**: Add Python to your PATH during installation
- **Mac/Linux**: Use `python3` and `pip3` instead of `python` and `pip`

### Dependencies installation fails

```bash
# Try with --user flag
pip install --user flask requests beautifulsoup4 lxml selenium python-dotenv
```

### Port 5000 already in use

Edit `app.py` and change the port number:
```python
app.run(host='0.0.0.0', port=8080, debug=True)
```

### All platforms showing "Not Available"

This is expected behavior due to:
- Anti-scraping measures on these platforms
- Dynamic JavaScript content that requires browser automation
- IP blocking or rate limiting

## Future Enhancements

- 📱 Mobile app version (Android/iOS)
- 🤖 AI-powered product matching and recommendations
- 📊 Price history tracking
- 🔔 Price drop alerts
- 💾 Save favorite products
- 📤 Export comparison results to PDF/Excel
- 🌍 Browser automation for JavaScript-heavy sites

## Technical Stack

- **Backend**: Flask (Python web framework)
- **Scraping**: BeautifulSoup4, lxml, requests
- **Frontend**: HTML, CSS, JavaScript, Bootstrap 5
- **Browser Automation**: Selenium (for future use)

## Project Structure

```
grocery-price-comparison/
├── app.py                 # Main Flask application
├── scrapers.py            # Web scraping functions for all platforms
├── templates/
│   └── index.html        # Main web interface
├── static/
│   ├── css/
│   │   └── style.css     # Custom styling
│   └── js/
│       └── script.js     # Frontend JavaScript
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## License

This project is for educational purposes only. Please respect the terms of service of the platforms being scraped.
