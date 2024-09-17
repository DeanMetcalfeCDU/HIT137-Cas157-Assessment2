import csv
from collections import Counter


def count_words(input_file_path, output_csv_path):
    """
    Counts the occurrences of words in a text file and stores the top 30 most common words
    in a CSV file.

    Parameters:
        input_file_path (str): Path to the input text file.
        output_csv_path (str): Path to the output CSV file.

    Returns:
        None
    """
    word_counter = Counter()  # Initialize a Counter to count words

    try:
        with open(input_file_path, 'r', encoding='utf-8') as file:
            line_count = 0
            for line in file:
                # Strip whitespace and check if the line is not empty
                line = line.strip()
                if not line:
                    continue  # Skip empty lines

                try:
                    # Tokenize the line into words and count them
                    words = line.lower().split()  # Convert to lowercase and split by whitespace
                    word_counter.update(words)  # Update the counter with words
                except Exception as e:
                    print(f"Error processing line {line_count}: {e}")

                line_count += 1
                # Output progress every 1000 lines
                if line_count % 1000 == 0:
                    print(f"Processed {line_count} lines...")

        # Write the top 30 most common words to the CSV file
        with open(output_csv_path, 'w', newline='', encoding='utf-8') as output_file:
            writer = csv.writer(output_file)
            writer.writerow(['Word', 'Count'])  # Write the header
            writer.writerows(word_counter.most_common(30))  # Write the top 30 words

        print(f"Successfully written the top 30 words to {output_csv_path}")

    except FileNotFoundError:
        print(f"Error: The input file '{input_file_path}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred during processing: {e}")


def main():
    input_file_path = 'C:/Users/deanm/OneDrive/CDU/Sem2-24/HIT137/Assessments/Assessment 2/combined_text.txt'
    output_csv_path = 'C:/Users/deanm/OneDrive/CDU/Sem2-24/HIT137/Assessments/Assessment 2/top_30_words.csv'
    count_words(input_file_path, output_csv_path)


if __name__ == "__main__":
    main()
