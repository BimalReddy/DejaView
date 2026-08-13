import os
from .pdf_parser import extract_text_from_pdf
from .docx_parser import extract_text_from_docx

def extract_text(file_path):
    """
    Routes the file to the correct parser based on its extension.
    """
    _, ext = os.path.splitext(file_path.lower())
    
    if ext == '.pdf':
        return extract_text_from_pdf(file_path)
    elif ext == '.docx':
        return extract_text_from_docx(file_path)
    else:
        raise ValueError(f"Unsupported file format: {ext}")
