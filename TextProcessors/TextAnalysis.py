# imports
import os
import fitz  # PyMuPDF for PDF files
from docx import Document  # python-docx for DOCX files

def convert_pdf_to_text(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text

def convert_txt_to_text(txt_path):
    with open(txt_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def convert_docx_to_text(docx_path):
    doc = Document(docx_path)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + '\n'
    return text

def convert_file_to_text(file_path):
    # Determine the file extension
    _, file_extension = os.path.splitext(file_path)
    
    # Based on the file extension, call the appropriate conversion function
    if file_extension.lower() == '.pdf':
        return convert_pdf_to_text(file_path)
    elif file_extension.lower() == '.txt':
        return convert_txt_to_text(file_path)
    elif file_extension.lower() == '.docx':
        return convert_docx_to_text(file_path)
    else:
        raise ValueError(f'Unsupported file type: {file_extension}')

def get_text_summary(string_text):
    return "Nothing for now"

def get_text_surrounding_topics(string_text):
    return ["nothing", "nope"]

def get_text_tone(string_text):
    return "normal"

if __name__ == "__main__":
    print("This script is being run as the main program.")
else:
    print("This script is being imported as a module.")
