# document_processor.py

import os
import numpy as np
from PyPDF2 import PdfReader
from docx import Document
from gensim.models import KeyedVectors

class DocumentProcessor:
    def __init__(self):
        # Load a pre-trained Word2Vec model (you can replace this with any model)
        self.model = KeyedVectors.load_word2vec_format('path/to/your/word2vec/model.bin', binary=True)

    def read_document(self, file_path):
        ext = os.path.splitext(file_path)[1].lower()
        if ext == '.pdf':
            return self.read_pdf(file_path)
        elif ext == '.docx':
            return self.read_docx(file_path)
        elif ext == '.txt':
            return self.read_txt(file_path)
        else:
            raise ValueError("Unsupported file type")

    def read_pdf(self, file_path):
        with open(file_path, 'rb') as f:
            reader = PdfReader(f)
            return "\n".join(page.extract_text() for page in reader.pages)

    def read_docx(self, file_path):
        doc = Document(file_path)
        return "\n".join(paragraph.text for paragraph in doc.paragraphs)

    def read_txt(self, file_path):
        with open(file_path, 'r') as f:
            return f.read()

    def create_embedding(self, text):
        words = text.split()
        vectors = []
        for word in words:
            if word in self.model:
                vectors.append(self.model[word])
        return np.mean(vectors, axis=0) if vectors else np.zeros(self.model.vector_size
