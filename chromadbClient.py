import chromadb
class ChromaDBClient:
    def __init__(self,path,collection_name,embedding_function):
        self.path=path
        self.collection_name=collection_name
        self.embedding_function=embedding_function
        self.client = chromadb.PersistentClient( self.path)
        self.collection = self.client.get_or_create_collection(
            name=self.collection_name, embedding_function= self.embedding_function
        )
    def add_documents(self,documents):
        for doc in documents:
            print("==== Inserting chunks into db;;; ====")
            self.collection.upsert(
                ids=[doc["id"]], documents=[doc["text"]], embeddings=[doc["embedding"]]
            )
    def query_documents(self,question, n_results=2):
        # query_embedding = get_openai_embedding(question)
        results = self.collection.query(query_texts=question, n_results=n_results)

        # Extract the relevant chunks
        relevant_chunks = [doc for sublist in results["documents"] for doc in sublist]
        print("==== Returning relevant chunks ====")
        return relevant_chunks
        # for idx, document in enumerate(results["documents"][0]):
        #     doc_id = results["ids"][0][idx]
        #     distance = results["distances"][0][idx]
        #     print(f"Found document chunk: {document} (ID: {doc_id}, Distance: {distance})")