import os
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)

CACHE_DIR = os.environ.get("CACHE_DIR", "cache")
CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 100))
MODEL_NAME = os.environ.get("MODEL_NAME", "paraphrase-distilroberta-base-v1")
FAISS_INDEX_TYPE = os.environ.get("FAISS_INDEX_TYPE", "ivfflat")
BOOK_PATH = os.environ.get("BOOK_PATH", "book.pdf")
API_KEY = os.environ.get("OPENAI_API_KEY", None)


BOOK_DETAILS = "This is the book 'The Network State' by Balaji Srinivasan."
