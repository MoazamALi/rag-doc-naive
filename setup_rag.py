import os
from dotenv import load_dotenv
from chromadb.utils import embedding_functions
import helper
from openaiClient import OpenAiClient
from chromadbClient import ChromaDBClient
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# get a object of openai wrapper
client = OpenAiClient(api_key=OPENAI_API_KEY)
openai_ef = embedding_functions.OpenAIEmbeddingFunction(
    api_key=OPENAI_API_KEY, model_name="text-embedding-3-small"
)
chromadb_client = ChromaDBClient(
    path="chroma_persistent_storage",
    collection_name="document_qa_collection",
    embedding_function=openai_ef
)

# Load documents from the directory
directory_path = "./data/news_articles"
documents = helper.load_documents_from_directory(directory_path)
print(f"Loaded {len(documents)} documents")
# Split documents into chunks
chunk_size = 1000
chunked_documents = helper.split_documents(documents, chunk_size)
print(f"Split documents into {len(chunked_documents)} chunks")


# Generate embeddings for the document chunks
for doc in chunked_documents:
    print("==== Generating embeddings... ====")
    doc["embedding"] = client.get_openai_embedding(doc["text"])


chromadb_client.add_documents(chunked_documents)

