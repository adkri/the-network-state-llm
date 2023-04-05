import faiss
import os
import numpy as np

def store_embeddings(embeddings, text_chunks, cache_dir):
    os.makedirs(cache_dir, exist_ok=True)

    index = faiss.IndexFlatL2(len(embeddings[0]))
    index.add(np.array(embeddings).astype('float32'))
    index_file_path = os.path.join(cache_dir, 'faiss_index')
    faiss.write_index(index, index_file_path)

    embeddings_cache_path = os.path.join(cache_dir, 'text_chunks.txt')
    with open(embeddings_cache_path, 'w') as cache_file:
        for chunk in text_chunks:
            cache_file.write(f"{chunk}\n")
    
    return index

def load_faiss_index(cache_dir):
    return faiss.read_index(f"{cache_dir}/faiss_index")
