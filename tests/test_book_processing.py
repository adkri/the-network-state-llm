import pytest
from llm_chat.book_processing import process_book, preprocess_text

def test_preprocess_text():
    text = "Hello, World! This is a sample text."
    expected_output = "hello world this is a sample text"
    assert preprocess_text(text) == expected_output

def test_process_book():
    # Assuming a sample book is present in the parent directory
    file_path = "../book.pdf"
    chunks = process_book(file_path)
    
    # Verify chunks are processed and preprocessed correctly
    for chunk in chunks:
        assert "  " not in chunk
        assert chunk.islower()
