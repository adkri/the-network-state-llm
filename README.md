# The Network State LLM Chat

The Network State LLM Chat is a Python-based project that creates a chat interface for [the network state book](https://thenetworkstate.com). It processes the book, divides it into chunks, and creates embeddings using Hugging Face's Sentence-BERT. The embeddings are stored using the FAISS library on disk in the cache/ directory. The chat interface is a simple Python terminal TUI that uses a Language Model API to answer user queries based on the book's context.

![Screenshot](images/screenshot.png)


## Architecture
The project consists of several components:

- book_processing.py: Handles processing of the PDF file and extracts text in chunks.
- sbert_embeddings.py: Creates embeddings for the text chunks using Sentence-BERT.
- faiss_storage.py: Stores the embeddings in a FAISS index on disk.
- chat_interface.py: Implements a simple terminal-based chat interface.
- config.py: Contains configuration variables such as the book path and cache directory.
- llm_api.py: Provides a function to complete prompts using a Language Model API.
- cli.py: Orchestrates the execution of the different components.


## Prerequisites
To run the project locally, you need to have Python 3.7 or higher installed. You also need to install the required Python libraries.

You can setup your system by following the instructions below.

### Setup
Clone the repository and download the book PDF file:
```sh
# Get the code
$ git clone https://github.com/adkri/the-network-state-llm.git
$ cd the-network-state-llm

# Download the network state book
$ curl -o book.pdf https://book.thenetworkstate.com/tns.pdf
```

We need to setup a Python virtual environment to 
```sh
$ python3 -m venv venv             # Create the virtual environment
$ source venv/bin/activate         # Activate it
$ pip install -r requirements.txt # Install the dependencies
```

### Running it locally
> You will need a API key from OpenAI. You can get one by signing up at [https://platform.openai.com/](https::/platform.openai.com/). Once you have the key, you can then add it to a .env file in the root directory of the project:
```sh
$ cp .env.example .env  # create the .env file and add your API key
```
Or include it when running the script.
```sh
$ OPENAI_API_KEY=... python3 cli.py
```

The script will process the book, create embeddings, and store them in the FAISS index. Once it's done, the chat interface will appear, and you can start asking questions about the book.

To exit the chat interface, type "exit".



## How it works: Faiss, Embeddings, and LLM API

Our project employs an efficient architecture combining Faiss, embeddings, and a Language Model API (LLM) to deliver an intelligent AI chat interface for book-related queries. Here's a simplified overview:

1. **Embeddings**: Embeddings are dense vector representations of text, generated using natural language processing techniques. We use Hugging Face's Sentence-BERT (SBERT) model to create embeddings for the book's text. SBERT, a modification of BERT, is designed specifically to produce sentence embeddings for direct similarity comparison, allowing efficient searches for the most relevant passages with Faiss.

2. **Faiss Library**: Developed by Facebook AI Research, Faiss is designed for efficient similarity search and clustering of dense vectors in large datasets. It helps us quickly find the most relevant text passages from the book by creating an **index** of the SBERT embeddings. This allows us to perform fast and efficient similarity searches to find the most relevant passages for a given user query.

3. **LLM API**: The Language Model API (LLM) is an interface to advanced natural language processing models like OpenAI's GPT-3. It's used to create AI responses based on relevant text passages found using Faiss and embeddings. The LLM model understands the context of the text, generating meaningful responses to user queries.

In essence, our architecture fuses Faiss, embeddings, and the LLM API to deliver an AI chat interface capable of providing precise book-related answers. Faiss and embeddings allow fast similarity searches for relevant passages, while the LLM API generates context-aware responses, creating a helpful chat interface even when dealing with large amounts of text.


## Co-Authors
- adkri
- GPT-4

## License
This project is released under the MIT License. See the LICENSE file for more information.  

