import docx
import logging

def extract_text_from_docx(file_path):
    """
    Reads a DOCX file and extracts all paragraph text.
    """
    text = ""
    try:
        doc = docx.Document(file_path)
        
        # Loop through paragraphs and extract text
        for para in doc.paragraphs:
            if para.text.strip():
                text += para.text.strip() + "\n"
                
        return text.strip()
        
    except Exception as e:
        logging.error(f"Error reading DOCX {file_path}: {e}")
        return ""
