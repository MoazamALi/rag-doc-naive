import os
# Function to load documents from a directory
def load_documents_from_directory(directory_path):
    print("==== Loading documents from directory ====")
    documents = []
    for filename in os.listdir(directory_path):
        if filename.endswith(".txt"):
            with open(
                os.path.join(directory_path, filename), "r", encoding="utf-8"
            ) as file:
                documents.append({"id": filename, "text": file.read()})
    return documents


def split_text(text, chunk_size=1000, chunk_overlap=20):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - chunk_overlap
    return chunks

def split_documents(documents, chunk_size=1000, chunk_overlap=20):
    split_documents = []
    for document in documents:
        chunks = split_text(document["text"], chunk_size, chunk_overlap)
        for chunk in chunks:
            split_documents.append({"id": document["id"], "text": chunk})
    return split_documents


