# Quick Start Guide

## Running on Replit (Easiest)

1. Click the **Run** button at the top of the Replit interface
2. Wait for the app to start (you'll see "Running on http://0.0.0.0:5000")
3. The app will automatically open in the webview
4. Try searching for products like: `milk`, `bread`, `maggi`, `butter`, or `rice`

## Running Locally on Your Laptop

### Step 1: Download the Project
- Click the **three dots menu** in Replit → **Download as ZIP**
- Extract the ZIP file to a folder on your computer

### Step 2: Install Python (if needed)
- **Windows**: Download from https://python.org/downloads/ (Make sure to check "Add Python to PATH")
- **Mac**: Already installed, or use `brew install python3`
- **Linux**: `sudo apt-get install python3 python3-pip`

### Step 3: Open Terminal/Command Prompt
- **Windows**: Press `Win + R`, type `cmd`, press Enter
- **Mac**: Press `Cmd + Space`, type `terminal`, press Enter
- **Linux**: Press `Ctrl + Alt + T`

### Step 4: Navigate to Project Folder
```bash
cd path/to/grocery-price-comparison
```
Replace `path/to/grocery-price-comparison` with your actual folder path

### Step 5: Install Dependencies
```bash
pip install flask requests beautifulsoup4 lxml selenium python-dotenv
```

If that doesn't work, try:
```bash
pip3 install flask requests beautifulsoup4 lxml selenium python-dotenv
```

### Step 6: Run the App
```bash
python app.py
```

If that doesn't work, try:
```bash
python3 app.py
```

### Step 7: Open in Browser
- Open your web browser (Chrome, Firefox, Edge, etc.)
- Go to: `http://localhost:5000`
- You should see the Grocery Price Comparison app!

## Using the App

1. Enter a product name in the search box (e.g., "Amul milk 1L")
2. Click **Search Prices**
3. Wait a few seconds for results
4. View the price comparison table
5. The best deal will be highlighted in **green**

## Demo Mode

By default, the app runs in **Demo Mode** and shows realistic sample data. This is because:
- Real grocery platforms block automated scraping
- They require JavaScript, location selection, and anti-bot verification
- Demo mode lets you see how the app works without these issues

### Trying Real Scraping (Advanced)

⚠️ **Warning**: Real scraping will likely fail

1. Open `scrapers.py` in a text editor
2. Find the line: `DEMO_MODE = True`
3. Change it to: `DEMO_MODE = False`
4. Save the file
5. Restart the app

## Troubleshooting

### "python is not recognized" or "pip is not recognized"
- Make sure Python is installed and added to PATH
- Try using `python3` and `pip3` instead

### Port 5000 already in use
- Edit `app.py`, change port 5000 to 8080 (or any other number)
- Then go to `http://localhost:8080` in your browser

### Dependencies won't install
- Try: `pip install --user flask requests beautifulsoup4 lxml selenium python-dotenv`

### Need help?
- Check the full `README.md` file for more detailed instructions
- Make sure you're in the correct folder when running commands
- On Windows, try running Command Prompt as Administrator

## Editing in VS Code

1. Install VS Code from: https://code.visualstudio.com/
2. Open VS Code
3. Click **File** → **Open Folder**
4. Select your grocery-price-comparison folder
5. Edit any file by clicking on it in the sidebar
6. Save changes with `Ctrl + S` (or `Cmd + S` on Mac)
7. To run the app, open the terminal in VS Code (`Ctrl + ~`) and type `python app.py`

## What You Can Do Next

- **Customize prices**: Edit the `demo_prices` dictionary in `scrapers.py`
- **Add more products**: Add entries to the demo data
- **Change styling**: Edit `static/css/style.css` to change colors and design
- **Modify UI**: Edit `templates/index.html` to change the layout
- **Export results**: Add a button to download comparison as CSV (future feature)
- **Price history**: Track prices over time (future feature)
- **Mobile app**: Convert to React Native or Flutter (future feature)

Enjoy your price comparison app! 🛒
