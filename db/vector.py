import os
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

QDRANT_HOST = os.getenv("QDRANT_HOST", "localhost")
QDRANT_PORT = os.getenv("QDRANT_PORT", "6335") # Using the mapped port from docker-compose

try:
    client = QdrantClient(url=f"http://{QDRANT_HOST}:{QDRANT_PORT}", check_compatibility=False)
except Exception as e:
    print(f"Failed to connect to Qdrant: {e}")
    client = None

def init_collections():
    if not client:
        return
    try:
        collections = [c.name for c in client.get_collections().collections]
        if "documents" not in collections:
            client.create_collection(
                collection_name="documents",
                vectors_config=VectorParams(size=768, distance=Distance.COSINE)
            )
            print("Qdrant collection 'documents' created.")
        else:
            print("Qdrant collection 'documents' already exists.")
    except Exception as e:
        print(f"Skipping Qdrant init due to connection error: {e}")

def search_documents(query_vector: list, limit: int = 5):
    if not client:
        return []
    return client.search(
        collection_name="documents",
        query_vector=query_vector,
        limit=limit
    )

if __name__ == "__main__":
    init_collections()
