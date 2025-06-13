# Scopus API Configuration Template
# Copy this file to config.py and fill in your credentials

# Your Scopus API credentials from Elsevier Developer Portal
SCOPUS_API_KEY = "YOUR_API_KEY_HERE"
AUTHOR_ID = "YOUR_AUTHOR_ID_HERE"

# API configuration
API_BASE_URL = "https://api.elsevier.com/content"
REQUEST_HEADERS = {"X-ELS-APIKey": SCOPUS_API_KEY, "Accept": "application/json"}

# Rate limiting configuration
API_DELAY = 0.5  # seconds between API calls
BATCH_SIZE = 25  # publications per API request
