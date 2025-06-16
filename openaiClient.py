from openai import OpenAI
class OpenAiClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.client = OpenAI(api_key=api_key)

    
    def get_openai_embedding(self, text):
        print("==== Generating embeddings... ====")
        response = self.client.embeddings.create(input=text, model="text-embedding-3-small")
        embedding = response.data[0].embedding
        return embedding
    
    def generate_response(self, question, relevant_chunks):
        context = "\n\n".join(relevant_chunks)
        prompt = (
            "You are an assistant for question-answering tasks. Use the following pieces of "
            "retrieved context to answer the question. If you don't know the answer, say that you "
            "don't know. Use three sentences maximum and keep the answer concise."
            "\n\nContext:\n" + context + "\n\nQuestion:\n" + question
        )

        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": question}
            ]
        )

        answer = response.choices[0].message.content
        return answer