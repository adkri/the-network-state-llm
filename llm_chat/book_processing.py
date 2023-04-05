import PyPDF2
import re
import logging

logger = logging.getLogger(__name__)

def preprocess_text(text):
    # Remove special characters and extra whitespace
    text = re.sub(r'\W+', ' ', text)
    # Convert to lowercase
    text = text.lower()
    text = text.strip()
    return text

def process_book(file_path, chunk_size=1):
    try:
        with open(file_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            text_chunks = []
            current_chunk = ""
            for page in reader.pages:
                current_chunk += page.extract_text()

                if len(current_chunk.split()) >= chunk_size:
                    text_chunks.append(preprocess_text(current_chunk))
                    current_chunk = ""

            if current_chunk:
                text_chunks.append(preprocess_text(current_chunk))

    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        return []

    return text_chunks
