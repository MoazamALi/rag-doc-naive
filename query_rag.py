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

question = "tell me about databricks"
relevant_chunks = chromadb_client.query_documents(question)
answer = client.generate_response(question, relevant_chunks)

print(answer)
