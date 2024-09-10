# vector_database.py

import chromadb

class VectorDatabase:
    def __init__(self):
        self.client = chromadb.Client()
        self.collection = self.client.create_collection(name="documents")

    def store_embedding(self, asset_id, embedding, metadata):
        self.collection.add(
            documents=[metadata['file_name']],
            embeddings=[embedding],
            metadatas=[metadata],
            ids=[asset_id]
        )

    def query_embedding(self, query_embedding, n_results=5):
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results
        )
        return results
