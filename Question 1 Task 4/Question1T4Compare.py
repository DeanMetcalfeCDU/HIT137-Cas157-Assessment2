# https://github.com/DeanMetcalfeCDU/HIT137-Cas157-Assessment2
# Created by Dean Metcalfe

import json


# Function to load entities from a JSON file
def load_entities(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return set(data['diseases'])


# Function to compare entities and print results
def compare_entities(scispacy_file, biobert_file):
    # Load entities from the files
    scispacy_diseases = load_entities(scispacy_file)
    biobert_diseases = load_entities(biobert_file)

    # Calculate totals
    total_scispacy = len(scispacy_diseases)
    total_biobert = len(biobert_diseases)

    # Find common and unique entities
    common_entities = scispacy_diseases.intersection(biobert_diseases)
    unique_to_scispacy = scispacy_diseases - biobert_diseases
    unique_to_biobert = biobert_diseases - scispacy_diseases

    # Print results
    print(f"Total diseases extracted by SciSpacy: {total_scispacy}")
    print(f"Total diseases extracted by BioBERT: {total_biobert}")
    print(f"Number of common diseases: {len(common_entities)}")
    print(f"Number of diseases unique to SciSpacy: {len(unique_to_scispacy)}")
    print(f"Number of diseases unique to BioBERT: {len(unique_to_biobert)}")

    # Print some example entities
    print("\nExamples of common diseases:", list(common_entities)[:10])
    print("\nExamples of diseases unique to SciSpacy:", list(unique_to_scispacy)[:10])
    print("\nExamples of diseases unique to BioBERT:", list(unique_to_biobert)[:10])


# Main function
def main():
    scispacy_file = 'C:/Users/deanm/OneDrive/CDU/Sem2-24/HIT137/Assessments/Assessment 2/scispacy_disease_entities.json'
    biobert_file = 'C:/Users/deanm/OneDrive/CDU/Sem2-24/HIT137/Assessments/Assessment 2/biobert_disease_entities.json'

    # Compare entities extracted by SciSpacy and BioBERT
    compare_entities(scispacy_file, biobert_file)


if __name__ == '__main__':
    main()
