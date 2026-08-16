import os
import logging
import argparse

# Import our custom modules
from extractors import extract_text
from nlp.preprocessor import preprocess_text
from nlp.similarity import compute_similarity
from utils.file_manager import get_submission_files
from utils.report_gen import format_report, save_report_as_json, print_cli_summary

# Configure basic logging to see what the script is doing
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def main():
    # Setup argument parser for flexible command line execution
    parser = argparse.ArgumentParser(description="School Plagiarism Checker Backend")
    parser.add_argument('--uploads-dir', type=str, default=os.path.join('data', 'uploads'), 
                        help="Path to the folder containing student submissions")
    parser.add_argument('--report-file', type=str, default='plagiarism_report.json', 
                        help="Path to save the output JSON report")
    parser.add_argument('--threshold', type=float, default=70.0, 
                        help="Similarity percentage threshold to flag suspicious matches")
    
    args = parser.parse_args()

    uploads_dir = args.uploads_dir
    report_file = args.report_file
    threshold = args.threshold

    logging.info(f"Scanning directory: {uploads_dir}")
    
    # 1. Gather all submitted files
    files = get_submission_files(uploads_dir)
    if not files:
        logging.error("No valid PDF or DOCX files found in '{uploads_dir}'. Exiting.")
        return

    logging.info("Found {len(files)} files. Starting extraction and NLP processing...")

    # 2. Extract and Preprocess text for every file
    processed_docs = {}
    for file_path in files:
        filename = os.path.basename(file_path)
        logging.info("Processing: {filename}")
        
        # Extract raw text
        raw_text = extract_text(file_path)
        if not raw_text:
            logging.warning("Could not extract text from {filename}. Skipping.")
            continue
            
        # Clean text (remove stopwords, punctuation, lemmatize)
        clean_text = preprocess_text(raw_text)
        if not clean_text:
            logging.warning("No usable text left after cleaning {filename}. Skipping.")
            continue
            
        # Store in our dictionary
        processed_docs[file_path] = clean_text

    # 3. Compute Similarity Scores
    logging.info("Calculating TF-IDF and Cosine Similarity scores...")
    similarity_results = compute_similarity(processed_docs)

    if not similarity_results:
        logging.warning("Not enough valid documents to perform a comparison. Exiting.")
        return

    # 4. Generate and Output Reports
    logging.info("Generating final report...")
    report_data = format_report(similarity_results, threshold=threshold)
    
    # Print nice table to the terminal
    print_cli_summary(report_data)
    
    # Save structured data to JSON (useful if sending to a web frontend later)
    save_report_as_json(report_data, report_file)


if __name__ == "__main__":
    main()
