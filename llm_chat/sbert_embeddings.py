import os
from sentence_transformers import SentenceTransformer
from llm_chat.config import CACHE_DIR

MODEL_NAME = 'paraphrase-distilroberta-base-v1'
MODEL_CACHE_DIR = os.path.join(CACHE_DIR, "sbert_model")

def create_embeddings(text_chunks):
    """
    Create embeddings for the given text chunks using the SentenceTransformer model.
    
    Args:
        text_chunks (list): A list of text chunks for which embeddings need to be created.
        
    Returns:
        numpy.ndarray: An array of embeddings corresponding to the input text chunks.
    """
    model = SentenceTransformer(MODEL_NAME, cache_folder=MODEL_CACHE_DIR)
    embeddings = model.encode(text_chunks)
    return embeddings
