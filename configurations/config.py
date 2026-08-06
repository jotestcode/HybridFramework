import os
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / '.env')

# UI
homepageurl = os.getenv("HOME_PAGE_URL")
loginpageurl = os.getenv("LOGIN_PAGE_URL")
miscellaneouspageurl = os.getenv("MISC_UI_PAGE_URL")

username = os.getenv("UI_USERNAME")
password = os.getenv("UI_PASSWORD")
invalid_username = os.getenv("INVALID_USERNAME")

# API
apipageUrl = os.getenv("API_BASE_URL")
api_token = os.getenv("API_TOKEN")