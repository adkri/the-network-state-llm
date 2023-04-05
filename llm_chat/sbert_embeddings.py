from sentence_transformers import SentenceTransformer

from llm_chat.config import CACHE_DIR

MODEL_NAME = 'paraphrase-distilroberta-base-v1'
MODEL_CACHE_DIR = CACHE_DIR + "/sbert_model"

def create_embeddings(text_chunks):
    model = SentenceTransformer(MODEL_NAME, cache_folder=MODEL_CACHE_DIR)
    embeddings = model.encode(text_chunks)
    return embeddings
