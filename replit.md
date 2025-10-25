# Grocery Price Comparison App

## Project Overview
A Python Flask web application that compares grocery product prices across 5 major Indian delivery platforms:
- Zepto
- Blinkit
- BigBasket
- JioMart
- Swiggy Instamart

**Status**: Initial MVP implementation complete
**Created**: October 25, 2025
**Tech Stack**: Python 3.11, Flask, BeautifulSoup4, Bootstrap 5

## Project Architecture

### Backend Structure
- `app.py` - Main Flask application with routes
  - `/` - Home page (GET)
  - `/search` - Product search endpoint (POST, JSON)
- `scrapers.py` - Web scraping functions for all 5 platforms
  - Individual scraper functions for each platform
  - `scrape_all_platforms()` - Orchestrates all scrapers and determines best deal

### Frontend Structure
- `templates/index.html` - Main web interface with search form and results table
- `static/css/style.css` - Custom styling with gradient background and responsive design
- `static/js/script.js` - Frontend JavaScript for AJAX search and dynamic results display

### Key Features Implemented
1. Product search input interface
2. Simultaneous scraping from all 5 platforms
3. Side-by-side price comparison table
4. Best deal highlighting (green background)
5. Graceful error handling for blocked/unavailable platforms
6. Responsive design with Bootstrap 5
7. Platform-specific color-coded badges

## Important Notes

### Web Scraping Challenges
- Most platforms use JavaScript rendering and anti-scraping measures
- Success rate may be low due to platform restrictions
- App handles failures gracefully with error messages
- Future enhancement: Consider using Selenium for JavaScript-heavy sites

### Local Development
- App runs on `0.0.0.0:5000` for Replit compatibility
- Users can download and run locally with `python app.py`
- All dependencies listed in `requirements.txt`

## Recent Changes

### 2025-10-25: Initial Implementation
- Created Flask app with search endpoint
- Implemented scrapers for all 5 platforms
- Built responsive web UI with Bootstrap 5
- Added error handling and best deal detection
- Generated documentation (README.md)

## User Preferences
- User wants local execution (not cloud hosting)
- Prefers Python-based solution
- Interested in future mobile version and AI automation
- Needs VS Code/Replit setup instructions

## Dependencies
- flask - Web framework
- requests - HTTP requests
- beautifulsoup4 - HTML parsing
- lxml - Faster HTML parsing
- selenium - Browser automation (for future use)
- python-dotenv - Environment configuration

## Next Steps (Future Enhancements)
- Implement caching to avoid repeated scraping
- Add price history tracking
- Create export functionality (CSV/PDF)
- Develop mobile PWA version
- Integrate AI for product matching
- Consider Selenium for JavaScript-rendered pages
