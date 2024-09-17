# https://github.com/DeanMetcalfeCDU/HIT137-Cas157-Assessment2
# Created by Dean Metcalfe

import torch
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline
import spacy
import json

# Check if host system supports and is configured to use CUDA (NVIDIA) if so uses GPU processing, else use CPU processing.
try:
    scispacy_model = spacy.load("en_ner_bc5cdr_md")
    if torch.cuda.is_available():
        spacy.require_gpu()
    scispacy_model.max_length = 1500000  # Increase max_length to handle the large text file
    print(
        "SciSpacy model loaded successfully with GPU support." if torch.cuda.is_available() else "SciSpacy model loaded on CPU.")
except Exception as e:
    print(f"Error loading SciSpacy model: {e}")

# Function to split text by lines to create chunks with the aim of improving processing speed
def split_by_lines(text, lines_per_chunk=100):
    lines = text.splitlines()
    chunks = ['\n'.join(lines[i:i + lines_per_chunk]) for i in range(0, len(lines), lines_per_chunk)]
    print(f"Completed text splitting. Total chunks: {len(chunks)}")
    return chunks

# Function to extract chemicals using SciSpacy
def extract_chemicals_scispacy(input_file):
    extracted_chemicals = []

    try:
        print(f"Reading input file: {input_file}")
        with open(input_file, 'r') as file:
            text = file.read()

        print(f"File read successfully. Size: {len(text)} characters.")

        # Split the text by lines into smaller chunks
        chunks = split_by_lines(text, lines_per_chunk=100)

        for i, chunk in enumerate(chunks):
            try:
                doc = scispacy_model(chunk)
                # Extract entities labeled as 'CHEMICAL'
                for entity in doc.ents:
                    if entity.label_ == 'CHEMICAL':
                        extracted_chemicals.append(entity.text)
                # Prints chunks processed to track progress
                print(f"Processed chunk {i + 1} out of {len(chunks)}")
            except Exception as e:
                print(f"Error processing chunk {i + 1}: {e}")

    except Exception as e:
        print(f"Error reading input file: {e}")

    return extracted_chemicals

# Function to extract chemicals using BioBERT
def extract_chemicals_biobert(input_file, model_name='alvaroalon2/biobert_chemical_ner'):
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForTokenClassification.from_pretrained(model_name).to(device)

    # Set up the NER pipeline
    nlp_pipeline = pipeline(
        "ner",
        model=model,
        tokenizer=tokenizer,
        aggregation_strategy="simple",
        device=0 if torch.cuda.is_available() else -1
    )

    extracted_chemicals = []

    try:
        print(f"Reading input file: {input_file}")
        with open(input_file, 'r') as file:
            text = file.read()

        print(f"File read successfully. Size: {len(text)} characters.")

        # Split the text by lines into smaller chunks
        chunks = split_by_lines(text, lines_per_chunk=100)

        for i, chunk in enumerate(chunks):
            try:
                ner_results = nlp_pipeline(chunk)
                # Extract entities labeled as 'CHEMICAL'
                for result in ner_results:
                    entity_text = result['word']
                    entity_label = result['entity_group']
                    if entity_label == 'CHEMICAL':
                        extracted_chemicals.append(entity_text)
                # Prints chunks processed to track progress
                print(f"Processed chunk {i + 1} out of {len(chunks)}")
            except Exception as e:
                print(f"Error processing chunk {i + 1}: {e}")

    except Exception as e:
        print(f"Error reading input file: {e}")

    return extracted_chemicals

# Save entities to a JSON file
def save_entities_to_json(entities, output_file):
    try:
        with open(output_file, 'w') as file:
            json.dump({'chemicals': entities}, file, indent=4)
        print(f"Entities successfully saved to {output_file}")
    except Exception as e:
        print(f"Error saving entities to JSON file: {e}")

# Main function to run both extractions
def main():
    input_file = 'C:/Users/deanm/OneDrive/CDU/Sem2-24/HIT137/Assessments/Assessment 2/Question 1 Task 1/combined_text.txt' 

    # Extract chemicals using SciSpacy
    scispacy_chemicals = extract_chemicals_scispacy(input_file)
    save_entities_to_json(scispacy_chemicals, 'C:/Users/deanm/OneDrive/CDU/Sem2-24/HIT137/Assessments/Assessment 2/scispacy_chemical_entities_full.json')

    # Extract chemicals using BioBERT
    biobert_chemicals = extract_chemicals_biobert(input_file)
    save_entities_to_json(biobert_chemicals, 'C:/Users/deanm/OneDrive/CDU/Sem2-24/HIT137/Assessments/Assessment 2/biobert_chemical_entities_full.json')

    print("Extraction completed.")

if __name__ == '__main__':
    main()
