import PyPDF2
import logging

def extract_text_from_pdf(file_path):
    """
    Reads a PDF file and extracts all available text.
    """
    text = ""
    try:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            
            # Loop through all pages and extract text
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                extracted = page.extract_text()
                if extracted:
                    text += extracted + "\n"
                    
        return text.strip()
    
    except Exception as e:
        logging.error("Error reading PDF {file_path}: {e}")
        return ""
