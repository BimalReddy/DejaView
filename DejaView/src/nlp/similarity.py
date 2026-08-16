import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import logging

def compute_similarity(documents_dict):
    """
    Computes pairwise cosine similarity scores for a dictionary of preprocessed documents.

    :param documents_dict: Dict mapping file names to cleaned text 
                           e.g., {"doc1.pdf": "clean text...", "doc2.docx": "clean text..."}
    :return: A list of dicts with file pairs and their similarity percentage, sorted highest to lowest.
    """
    file_names = list(documents_dict.keys())
    texts = list(documents_dict.values())

    # We need at least 2 documents to make comparisons
    if len(texts) < 2:
        logging.warning("At least two documents are required to compute similarity.")
        return []

    # 1. Create the TF-IDF Vectorizer
    # ngram_range=(1, 2) looks at single words AND two-word pairs (captures copied phrases better)
    vectorizer = TfidfVectorizer(ngram_range=(1, 2))
    
    try:
        tfidf_matrix = vectorizer.fit_transform(texts)
    except ValueError as e:
        # Handles cases where all documents are empty after preprocessing
        logging.error(f"Error generating TF-IDF matrix: {e}")
        return []

    # 2. Compute Cosine Similarity Matrix
    similarity_matrix = cosine_similarity(tfidf_matrix)

    # 3. Extract unique pairs (avoiding self-comparison and duplicate reversed pairs)
    results = []
    num_docs = len(file_names)

    for i in range(num_docs):
        for j in range(i + 1, num_docs):
            doc1 = file_names[i]
            doc2 = file_names[j]
            score = float(similarity_matrix[i][j])
            
            # Convert decimal score (0.85) into a percentage (85.0%)
            similarity_percentage = round(score * 100, 2)

            results.append({
                "file_1": doc1,
                "file_2": doc2,
                "similarity_score": similarity_percentage
            })

    # 4. Sort results from highest similarity to lowest
    results.sort(key=lambda x: x["similarity_score"], reverse=True)

    return results


# Quick local test
if __name__ == "__main__":
    sample_docs = {
        "student_a.docx": "climate change impacts sea level rising global warming polar ice caps melt",
        "student_b.pdf": "climate change impacts sea level rising global warming polar ice caps melt fast",
        "student_c.docx": "python code structure requires modular design separated into packages and functions"
    }

    rankings = compute_similarity(sample_docs)
    for pair in rankings:
        print(f"{pair['file_1']} <-> {pair['file_2']}: {pair['similarity_score']}% match")
