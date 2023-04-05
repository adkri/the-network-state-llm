import numpy as np
import os
from llm_chat.sbert_embeddings import create_embeddings
from llm_chat.faiss_storage import load_faiss_index
from llm_chat.llm_api import prompt_completion
from llm_chat.config import CACHE_DIR, BOOK_DETAILS

import logging
logger = logging.getLogger(__name__)

def find_best_response(query, k=5):
    faiss_index = load_faiss_index(CACHE_DIR)
    if faiss_index is None:
        logging.error("Error: Could not load the FAISS index.")
        return

    query_embedding = create_embeddings([query])[0]
    D, I = faiss_index.search(np.array([query_embedding]), k)
    neighbors, distances = I.flatten().tolist(), D.flatten().tolist()

    # Retrieve the corresponding text_chunks stored on disk
    relevant_texts = []
    with open(os.path.join(CACHE_DIR, 'text_chunks.txt'), "r") as cache_file:
        for i, line in enumerate(cache_file):
            if i in neighbors:
                relevant_texts.append(line.strip())

    context = " ".join(relevant_texts)

    # Generate the prompt for the LLM
    prompt = f"{BOOK_DETAILS} The following passage from the book provides context: '{context}'. Based on this context, please answer the question: '{query}'"

    response = prompt_completion(context, prompt)
    return response
