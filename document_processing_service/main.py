# main.py

import os
import uuid
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from document_processor import DocumentProcessor
from vector_database import VectorDatabase

app = FastAPI()
processor = DocumentProcessor()
vector_db = VectorDatabase()

@app.post("/api/documents/process")
async def process_document(file: UploadFile = File(...)):
    file_path = f"temp/{file.filename}"
    
    # Save the uploaded file temporarily
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    try:
        text = processor.read_document(file_path)
        embedding = processor.create_embedding(text)
        asset_id = str(uuid.uuid4())
        
        metadata = {
            "file_name": os.path.basename(file_path),
            "file_path": file_path,
        }

        vector_db.store_embedding(asset_id, embedding.tolist(), metadata)
        return JSONResponse(content={"asset_id": asset_id})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        os.remove(file_path)  # Clean up the temporary file

