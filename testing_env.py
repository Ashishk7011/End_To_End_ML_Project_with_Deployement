from dotenv import load_dotenv
import os

load_dotenv()

print("ENV VALUE:", os.getenv("MONGO_DB_URL"))