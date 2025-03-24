# Resume Parser

A Python-based Resume Parser that extracts key details from PDF and DOCX resumes using Flask, spaCy, and python-docx.

## Features
- Extracts **Name, Email, Phone Number, and Skills** from resumes.
- Supports **PDF** and **DOCX** formats.
- Uses **spaCy NLP** for entity recognition.
- Simple **command-line interface** for easy usage.

## AI-Assisted Development
This project was efficiently developed using AI-powered coding assistance, which helped streamline the coding process, optimize performance, and accelerate development. Leveraging AI for software development enabled rapid prototyping and enhanced problem-solving.

## Installation
### Prerequisites
Make sure you have **Python 3.11+** installed.

### Step 1: Clone the Repository
```sh
git clone https://github.com/yourusername/resume-parser.git
cd resume-parser
```

### Step 2: Create a Virtual Environment & Activate It
```sh
python -m venv spacy_env
# Activate on Windows
spacy_env\Scripts\activate
# Activate on Mac/Linux
source spacy_env/bin/activate
```

### Step 3: Install Dependencies
```sh
pip install -r requirements.txt
```

### Step 4: Download spaCy Model
```sh
python -m spacy download en_core_web_sm
```

## Usage
Run the script and provide the path to a resume file:
```sh
python resume_parser.py
```
Follow the prompts to enter the file path, and the script will display extracted details.

## Example Output
```
Extracted Information:
Name: John Doe
Email: johndoe@example.com
Phone: +1 234-567-8901
Skills: Python, Machine Learning, Data Science
```

## Future Enhancements
- Improve skill extraction using machine learning.
- Add a web interface with Flask for easier usage.

## License
This project is licensed under the MIT License.
