# DejaView
Here is a comprehensive `README.md` file for your project. You can paste this directly into the root directory of your repository.

```markdown
# 🔍 School Portal Plagiarism Checker Backend

An in-house, Python-based plagiarism detection tool designed to extract text from student essay submissions (`.pdf` and `.docx`), clean and normalize the language using Natural Language Processing (NLP), and calculate pairwise similarity scores using TF-IDF vectorization and Cosine Similarity.

---

## 📌 Features

*   **Multi-Format File Parsing:** Extracts raw text from Microsoft Word (`.docx`) and Adobe PDF (`.pdf`) documents.
*   **NLP Text Preprocessing:** Uses `nltk` to lowercase text, strip punctuation, filter out English stopwords, and lemmatize words to their base roots.
*   **Smart Similarity Scoring:** Converts cleaned text into TF-IDF (Term Frequency-Inverse Document Frequency) matrices with unigrams and bigrams (`ngram_range=(1,2)`), followed by Cosine Similarity calculation.
*   **Flexible CLI & Reporting:** Set custom similarity thresholds, generate clean terminal summaries, and export structured JSON reports for frontend integration.
*   **Fully Tested:** Includes built-in unit tests for extractors and similarity scoring using Python's native `unittest` framework.

---

## 📁 Directory Structure

```text
school_plagiarism_checker/
│
├── data/                       # Local file storage
│   ├── uploads/                # Directory for raw incoming .pdf and .docx files
│   └── processed/              # Extracted/cached plain text files
│
├── src/                        # Main application source code
│   ├── __init__.py
│   ├── main.py                 # Pipeline execution script
│   │
│   ├── extractors/             # File extraction package
│   │   ├── __init__.py
│   │   ├── pdf_parser.py       # PyPDF2 extraction logic
│   │   └── docx_parser.py      # python-docx extraction logic
│   │
│   ├── nlp/                    # Natural Language Processing package
│   │   ├── __init__.py
│   │   ├── preprocessor.py     # Tokenization, stopword removal, lemmatization
│   │   └── similarity.py       # TF-IDF & Cosine Similarity calculation
│   │
│   └── utils/                  # Utility functions
│       ├── __init__.py
│       ├── file_manager.py     # File validation and directory cleaning
│       └── report_gen.py       # CLI summary formatting and JSON exporter
│
├── tests/                      # Automated test suite
│   ├── test_extractors.py
│   └── test_similarity.py
│
├── .gitignore                  # Git tracking exclusion configuration
├── requirements.txt            # Dependency manifest
└── README.md                   # Documentation

```

---

## ⚙️ Prerequisites & Installation

### 1. Requirements

* Python **3.8+**
* `pip` package manager

### 2. Setup Virtual Environment

Clone or download the project, navigate to the root directory, and set up a virtual environment:

```bash
# Navigate to project root
cd school_plagiarism_checker

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

```

### 3. Install Dependencies

Install all required libraries specified in `requirements.txt`:

```bash
pip install -r requirements.txt

```

---

## 🚀 How to Run

1. Place the student `.pdf` and `.docx` files you wish to compare into the `data/uploads/` directory.
2. Execute the main pipeline script from the root directory:

```bash
python src/main.py

```

### Command-Line Arguments

Customize execution parameters using command-line flags:

| Parameter | Default | Description |
| --- | --- | --- |
| `--uploads-dir` | `data/uploads` | Path to the directory containing student files |
| `--threshold` | `70.0` | Similarity score percentage threshold to flag suspicious submissions |
| `--report-file` | `plagiarism_report.json` | Path where the exported JSON summary will be saved |

#### Example Usage with Arguments:

```bash
python src/main.py --uploads-dir "path/to/essays" --threshold 65.0 --report-file "data/processed/report.json"

```

---

## 📊 Sample Output

### Terminal Summary Output

```text
============================================================
           PLAGIARISM DETECTION SUMMARY REPORT           
============================================================
Total Files Compared Pairwise: 3
Flagged Matches (>= 70.0%): 1
------------------------------------------------------------
File 1                    File 2                    Match Score 
------------------------------------------------------------
essay_student_A.docx      essay_student_B.pdf       88.45%     [FLAGGED]
essay_student_A.docx      essay_student_C.docx      12.10%    
essay_student_B.pdf       essay_student_C.docx      11.05%    
============================================================

```

### JSON Export (`plagiarism_report.json`)

```json
{
    "total_comparisons": 3,
    "total_flagged": 1,
    "threshold_used": 70.0,
    "flagged_matches": [
        {
            "file_1": "essay_student_A.docx",
            "file_2": "essay_student_B.pdf",
            "similarity_score": 88.45,
            "flagged": true
        }
    ],
    "all_results": [ ... ]
}

```

---

## 🧪 Running Unit Tests

Run the full automated test suite from the root directory using Python's `unittest` module:

```bash
python -m unittest discover -s tests

```

---

## 🔬 How the Algorithmic Pipeline Works

1. **Text Extraction:** `PyPDF2` and `python-docx` extract raw strings from uploaded submission files.
2. **Text Preprocessing:**
* Converts all text to lowercase.
* Strips numbers, special characters, and punctuation.
* Removes filler words (*stopwords*) using `nltk.corpus.stopwords`.
* Lemmatizes words using `nltk.stem.WordNetLemmatizer` (e.g., converts "writing", "wrote", "writes" to "write").


3. **Vectorization (TF-IDF):** Converted clean text strings into numerical vectors using `sklearn.feature_extraction.text.TfidfVectorizer` configured with 1-gram and 2-gram evaluation.
4. **Cosine Similarity Computation:** Computes dot products between document vectors using `sklearn.metrics.pairwise.cosine_similarity` to calculate normalized pairwise match percentages.

```

```


Note: The required libraries were suggested by AI and the README.md file is generated by AI.
