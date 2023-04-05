import os
import logging
import click
from llm_chat.book_processing import process_book
from llm_chat.sbert_embeddings import create_embeddings
from llm_chat.faiss_storage import store_embeddings
from llm_chat.config import CACHE_DIR, BOOK_PATH
from llm_chat.chat_interface import run_chat_interface

os.environ['TOKENIZERS_PARALLELISM'] = 'false'

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    if ctx.invoked_subcommand is None:
        if not os.path.exists(os.path.join(CACHE_DIR, 'faiss_index')):
            logger.info("Cache directory not found. Building the cache...")
            ctx.invoke(process_book_cmd)
        ctx.invoke(chat)

@click.command()
@click.option("--pdf-path", default=BOOK_PATH, help="Path to the PDF file.")
@click.option("--cache-dir", default=CACHE_DIR, help="Directory to store cache files.")
def process_book_cmd(pdf_path, cache_dir):
    text_chunks = process_book(pdf_path)
    embeddings = create_embeddings(text_chunks)
    store_embeddings(embeddings, text_chunks, cache_dir)

@click.command()
def chat():
    run_chat_interface()

cli.add_command(process_book_cmd, name="process_book")
cli.add_command(chat)

if __name__ == "__main__":
    cli()

