import csv
from collections import Counter
from transformers import AutoTokenizer


def count_unique_tokens(input_file_path, output_csv_path, model_name='bert-base-uncased'):
    """
    Counts the unique tokens in a text file using the AutoTokenizer from the transformers library
    and stores the top 30 most common tokens in a CSV file.

    Parameters:
        input_file_path (str): Path to the input text file.
        output_csv_path (str): Path to the output CSV file.
        model_name (str): The name of the pre-trained tokenizer model to use (default: 'bert-base-uncased').

    Returns:
        None
    """
    # Load the pre-trained tokenizer
    try:
        tokenizer = AutoTokenizer.from_pretrained(model_name)
    except Exception as e:
        print(f"Error loading the tokenizer: {e}")
        return

    token_counter = Counter()  # Initialize a Counter to count tokens

    try:
        with open(input_file_path, 'r', encoding='utf-8') as file:
            line_count = 0
            for line in file:
                line = line.strip()
                if not line:
                    continue  # Skip empty lines

                try:
                    # Tokenize the line and count tokens
                    tokens = tokenizer.tokenize(line)
                    token_counter.update(tokens)
                except Exception as e:
                    print(f"Error processing line {line_count}: {e}")

                line_count += 1
                # Output progress every 1000 lines
                if line_count % 1000 == 0:
                    print(f"Processed {line_count} lines...")

        # Write the top 30 most common tokens to the CSV file
        with open(output_csv_path, 'w', newline='', encoding='utf-8') as output_file:
            writer = csv.writer(output_file)
            writer.writerow(['Token', 'Count'])  # Write the header
            writer.writerows(token_counter.most_common(30))  # Write the top 30 tokens

        print(f"Successfully written the top 30 tokens to {output_csv_path}")

    except FileNotFoundError:
        print(f"Error: The input file '{input_file_path}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred during processing: {e}")


def main():
    input_file_path = 'C:/Users/deanm/OneDrive/CDU/Sem2-24/HIT137/Assessments/Assessment 2/combined_text.txt'
    output_csv_path = 'C:/Users/deanm/OneDrive/CDU/Sem2-24/HIT137/Assessments/Assessment 2/top_30_tokens.csv'
    count_unique_tokens(input_file_path, output_csv_path)


if __name__ == "__main__":
    main()
