import unittest
from src.nlp.preprocessor import preprocess_text
from src.nlp.similarity import compute_similarity

class TestNLP(unittest.TestCase):
    
    def test_preprocess_text(self):
        """Ensures punctuation is removed, text is lowercased, and words are lemmatized."""
        raw_text = "The QUICK brown foxes... jumped! 123"
        cleaned = preprocess_text(raw_text)
        
        # 'the' (stopword) and '123' (number) should be gone
        self.assertNotIn("the", cleaned)
        self.assertNotIn("123", cleaned)
        # 'foxes' should be reduced to 'fox'
        self.assertIn("fox", cleaned)
        # Should be completely lowercase
        self.assertEqual(cleaned, "quick brown fox jumped")

    def test_compute_similarity(self):
        """Ensures identical documents score 100% and different ones score much lower."""
        docs = {
            "student_1.txt": "artificial intelligence is the future of technology and machine learning",
            "student_2.txt": "artificial intelligence is the future of technology and machine learning", # Exact copy
            "student_3.txt": "baking a chocolate cake requires flour sugar and eggs" # Completely different
        }
        
        results = compute_similarity(docs)
        
        # 3 documents should result in 3 unique pairs (1v2, 1v3, 2v3)
        self.assertEqual(len(results), 3)
        
        for pair in results:
            if (pair["file_1"] == "student_1.txt" and pair["file_2"] == "student_2.txt") or \
               (pair["file_1"] == "student_2.txt" and pair["file_2"] == "student_1.txt"):
                # Exact matches should be ~100%
                self.assertGreaterEqual(pair["similarity_score"], 99.0)
            else:
                # Cake recipe vs AI should be 0%
                self.assertEqual(pair["similarity_score"], 0.0)

if __name__ == '__main__':
    unittest.main()
