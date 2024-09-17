import json
from collections import Counter

# Function to load drugs from a JSON file
def load_drugs_from_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            drugs = data.get('drugs', [])
        return drugs  # Return as a list to keep duplicates for counting
    except Exception as e:
        print(f"Error loading JSON file: {e}")
        return []

# Function to analyze drugs and find the most common ones
def analyze_drugs(scispacy_file):
    # Load drugs from SciSpacy file
    scispacy_drugs = load_drugs_from_json(scispacy_file)
    
    total_drugs = len(scispacy_drugs)
    print(f"Total drugs extracted by SciSpacy: {total_drugs}")

    # Count the occurrences of each drug
    drug_counter = Counter(scispacy_drugs)
    
    # Get the 10 most common drugs
    most_common_drugs = drug_counter.most_common(10)
    print("\nTop 10 most common drugs extracted by SciSpacy:")
    for drug, count in most_common_drugs:
        print(f"{drug}: {count}")

    return drug_counter

# Main function
def main():
    scispacy_file = 'C:/Users/deanm/OneDrive/CDU/Sem2-24/HIT137/Assessments/Assessment 2/Assessment 2 Project/Question 1 Task 4/scispacy_drug_entities.json'  # Path to the SciSpacy JSON file

    # Analyze SciSpacy drugs
    analyze_drugs(scispacy_file)

if __name__ == '__main__':
    main()
