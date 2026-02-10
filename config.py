# config.py
import os
from dotenv import load_dotenv

load_dotenv()

CHROMEDRIVER_PATH = os.getenv("CHROMEDRIVER_PATH")

if not CHROMEDRIVER_PATH:
    raise ValueError("CHROMEDRIVER_PATH is not set in .env file")
