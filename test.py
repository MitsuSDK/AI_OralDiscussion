from dotenv import load_dotenv
from pathlib import Path
import os
from openai import OpenAI

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

api_key = os.environ["OPENAI_API_KEY"]  # force error if missing
client = OpenAI(api_key=api_key)

print("OpenAI client initialized")
