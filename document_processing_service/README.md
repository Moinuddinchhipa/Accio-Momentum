# Document Processing Service with RAG Chatbot

## Setup Instructions

1. Clone the repository or create the directory structure as shown above.
2. Place your Word2Vec binary model in a folder accessible to the script and update the path in document_processor.py.
3. Install required packages:

   pip install -r requirements.txt
   
   Run the application

## API Endpoints

### Document Processing

- **POST /api/documents/process**
  - **Input**: File (PDF, DOCX, TXT)
  - **Output**: Asset ID

### Chat Service

- **POST /api/chat/start**
  - **Input**: Asset ID
  - **Output**: Chat thread ID

- **POST /api/chat/message**
  - **Input**: Chat thread ID, user message
  - **Output**: Agent response (streamed)

- **GET /api/chat/history**
  - **Input**: Chat thread ID
  - **Output**: Chat history

## Functional Overview

The service processes documents by reading their content, generating embeddings using a Word2Vec model, and storing these embeddings in a ChromaDB vector database. It also provides a chat service that allows users to interact with an agent based on the processed documents.
Final Steps

1. Run the Application: Execute the following command to start your FastAPI server:

   uvicorn main:app --reload
   

2. Test the API: Use Postman or curl to test the endpoints.

3. Potential Improvements:
   - Implement authentication for API access.
   - Use a proper database instead of in-memory storage for chat history.
   - Optimize embedding generation and retrieval.
   - Add more sophisticated error handling and logging.
