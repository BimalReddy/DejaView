import unittest
from unittest.mock import patch, MagicMock
from src.extractors.pdf_parser import extract_text_from_pdf
from src.extractors.docx_parser import extract_text_from_docx

class TestExtractors(unittest.TestCase):

    @patch('src.extractors.pdf_parser.PyPDF2.PdfReader')
    @patch('builtins.open', new_callable=unittest.mock.mock_open)
    def test_pdf_extractor(self, mock_open, mock_pdf_reader):
        """Mocks opening a PDF to ensure the parser extracts text correctly."""
        # Create a fake PDF page that returns specific text
        mock_page = MagicMock()
        mock_page.extract_text.return_value = "Fake PDF content."
        
        # Attach the fake page to our fake reader
        mock_reader_instance = MagicMock()
        mock_reader_instance.pages = [mock_page]
        mock_pdf_reader.return_value = mock_reader_instance
        
        # Run the function
        text = extract_text_from_pdf('dummy_path.pdf')
        
        # Check results
        self.assertEqual(text, "Fake PDF content.")
        mock_open.assert_called_once_with('dummy_path.pdf', 'rb')

    @patch('src.extractors.docx_parser.docx.Document')
    def test_docx_extractor(self, mock_docx_document):
        """Mocks opening a DOCX to ensure the parser iterates paragraphs correctly."""
        # Create a fake paragraph
        mock_para = MagicMock()
        mock_para.text = "Fake DOCX content."
        
        # Attach to the fake document
        mock_doc_instance = MagicMock()
        mock_doc_instance.paragraphs = [mock_para]
        mock_docx_document.return_value = mock_doc_instance
        
        # Run the function
        text = extract_text_from_docx('dummy_path.docx')
        
        # Check results
        self.assertEqual(text, "Fake DOCX content.")
        mock_docx_document.assert_called_once_with('dummy_path.docx')

if __name__ == '__main__':
    unittest.main()
