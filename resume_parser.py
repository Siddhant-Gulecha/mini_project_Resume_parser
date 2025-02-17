import re
import spacy
import PyPDF2
from docx import Document

# Load spaCy NLP model
nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file"""
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text

def extract_text_from_docx(docx_path):
    """Extract text from a DOCX file"""
    doc = Document(docx_path)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_email(text):
    """Extract email from text"""
    match = re.search(r"[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+", text)
    return match.group(0) if match else None

def extract_phone(text):
    """Extract phone number from text"""
    match = re.search(r"\+?\d{10,13}", text)  # Matches 10 to 13-digit numbers
    return match.group(0) if match else None

def extract_name(text):
    """Extract name from text using spaCy"""
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return None

def extract_skills(text):
    """Extract common programming skills"""
    skills = ["Python", "Java", "C++", "SQL", "JavaScript", "Machine Learning", "Deep Learning", "AI", "Data Science"]
    found_skills = [skill for skill in skills if skill.lower() in text.lower()]
    return found_skills

def parse_resume(file_path):
    """Parse resume and extract details"""
    if file_path.endswith(".pdf"):
        text = extract_text_from_pdf(file_path)
    elif file_path.endswith(".docx"):
        text = extract_text_from_docx(file_path)
    else:
        return "Unsupported file format"

    return {
        "Name": extract_name(text),
        "Email": extract_email(text),
        "Phone": extract_phone(text),
        "Skills": extract_skills(text),
    }

if __name__ == "__main__":
    file_path = input("Enter resume file path: ")
    parsed_data = parse_resume(file_path)
    print("\nExtracted Information:")
    for key, value in parsed_data.items():
        print(f"{key}: {value}")
