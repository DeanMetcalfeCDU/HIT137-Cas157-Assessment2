# https://github.com/DeanMetcalfeCDU/HIT137-Cas157-Assessment2
# Created by Dean Metcalfe

import os
import pandas as pd


def extract_text_from_csv(csv_file_paths, output_file_path):
    """
    Extracts the 'TEXT' column from multiple CSV files and writes all entries
    to a single output text file.

    Parameters:
        csv_file_paths (list): A list of paths to the input CSV files.
        output_file_path (str): Path to the output text file.
    """
    try:
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            for csv_file_path in csv_file_paths:
                # Check if the input CSV file exists
                if not os.path.exists(csv_file_path):
                    print(f"Error: The file {csv_file_path} does not exist. Skipping this file.")
                    continue

                try:
                    # Read the CSV file
                    df = pd.read_csv(csv_file_path)

                    # Check if 'TEXT' column exists
                    if 'TEXT' not in df.columns:
                        print(f"Warning: 'TEXT' column not found in {csv_file_path}. Skipping this file.")
                        continue

                    # Write each line in the 'TEXT' column to the output file as is
                    for line in df['TEXT']:
                        if pd.notna(line):  # Check if the line is not NaN
                            output_file.write(str(line) + '\n')

                except pd.errors.EmptyDataError:
                    print(f"Error: The file {csv_file_path} is empty.")
                except Exception as e:
                    print(f"An unexpected error occurred while processing {csv_file_path}: {e}")

        print(f"Successfully written all 'TEXT' entries to {output_file_path}")

    except Exception as e:
        print(f"An error occurred while writing to the output file: {e}")


def main():
    # List of input CSV file paths
    csv_file_paths = ['C:/Users/deanm/OneDrive/CDU/Sem2-24/HIT137/Assessments/Assessment 2/CSV1.csv', 'C:/Users/deanm/OneDrive/CDU/Sem2-24/HIT137/Assessments/Assessment 2/CSV2.csv', 'C:/Users/deanm/OneDrive/CDU/Sem2-24/HIT137/Assessments/Assessment 2/CSV3.csv', 'C:/Users/deanm/OneDrive/CDU/Sem2-24/HIT137/Assessments/Assessment 2/CSV4.csv']

    # Output file path
    output_file_path = 'C:/Users/deanm/OneDrive/CDU/Sem2-24/HIT137/Assessments/Assessment 2/Question 1 Task 1/combined_text.txt'

    # Extract text from CSV files and write to output file
    extract_text_from_csv(csv_file_paths, output_file_path)


if __name__ == "__main__":
    main()
