from collections import OrderedDict

def generate_text_report(analysis_result, output_path):
    """
    Generate a formatted text report.
    
    Sections:
    1. Document Overview
    2. Top Words
    3. Top Phrases (bigrams/trigrams)
    4. Readability Assessment
    """
    with open(output_path, 'w') as text_report:
        # Document Overview
        text_report.write("=== Document Overview ===\n")
        text_report.write(f"Total Words: {analysis_result['total_words']}\n")
        text_report.write(f"Unique Words: {analysis_result['unique_words']}\n")
        text_report.write(f"Average Word Length: {analysis_result['avg_word_length']:.2f}\n\n")

def generate_word_cloud_data(word_frequencies):
    """
    Prepare data for word cloud visualization.
    Returns: OrderedDict of word -> weight (ordered by frequency)
    """
    pass

def generate_frequency_table(word_frequencies):
    """
    Generate a formatted frequency table.
    Uses OrderedDict to maintain ranking order.
    """
    pass