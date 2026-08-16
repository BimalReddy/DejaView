import json
import os
import logging

def format_report(similarity_results, threshold=70.0):
    """
    Filters similarity results and flags file pairs that exceed the similarity threshold.
    """
    flagged_pairs = []
    
    for item in similarity_results:
        is_flagged = item["similarity_score"] >= threshold
        entry = {
            "file_1": os.path.basename(item["file_1"]),
            "file_2": os.path.basename(item["file_2"]),
            "similarity_score": item["similarity_score"],
            "flagged": is_flagged
        }
        
        if is_flagged:
            flagged_pairs.append(entry)

    summary = {
        "total_comparisons": len(similarity_results),
        "total_flagged": len(flagged_pairs),
        "threshold_used": threshold,
        "flagged_matches": flagged_pairs,
        "all_results": similarity_results
    }

    return summary


def save_report_as_json(report_data, output_filepath):
    """
    Saves the formatted report dictionary to a JSON file.
    """
    try:
        os.makedirs(os.path.dirname(output_filepath), exist_ok=True)
        with open(output_filepath, 'w', encoding='utf-8') as f:
            json.dump(report_data, f, indent=4)
        logging.info("Report successfully saved to {output_filepath}")
    except Exception as e:
        logging.error(f"Failed to save JSON report: {e}")


def print_cli_summary(report_data):
    """
    Prints a clean, scannable table to the console.
    """
    print("\n" + "="*60)
    print("           PLAGIARISM DETECTION SUMMARY REPORT           ")
    print("="*60)
    print(f"Total Files Compared Pairwise: {report_data['total_comparisons']}")
    print(f"Flagged Matches (>= {report_data['threshold_used']}%): {report_data['total_flagged']}")
    print("-" * 60)

    if not report_data["all_results"]:
        print("No document pairs to display.")
        return

    print(f"{'File 1':<25} {'File 2':<25} {'Match Score':<10}")
    print("-" * 60)

    for res in report_data["all_results"]:
        f1 = os.path.basename(res["file_1"])[:22]
        f2 = os.path.basename(res["file_2"])[:22]
        score = "{res['similarity_score']}%"
        
        # Mark suspicious entries with an asterisk
        flag_indicator = " [FLAGGED]" if res.get("flagged") else ""
        print(f"{f1:<25} {f2:<25} {score:<10}{flag_indicator}")

    print("="*60 + "\n")
