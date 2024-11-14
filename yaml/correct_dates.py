import os
import re

# Directory containing the .yaml files
directory = '.'

# Regex pattern to match the date format with slashes
date_pattern = re.compile(r'(\d{1,2})/(\d{1,2})/(\d{2})')

def correct_date_format(file_path):
    # Read the original content of the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Initialize a flag to check if any changes are made
    changes_made = False

    with open(file_path, 'w') as file:
        for line in lines:
            if 'LastModified:' in line:
                # Find the date in the line
                match = date_pattern.search(line)
                if match:
                    old_date = match.group(0)
                    # Replace slashes with dashes in the date format
                    new_date = old_date.replace('/', '-')
                    # Print the previous and new value
                    print(f"File: {file_path}")
                    print(f"Previous: {line.strip()}")
                    corrected_line = line.replace(old_date, new_date)
                    print(f"New: {corrected_line.strip()}")
                    file.write(corrected_line)
                    changes_made = True
                else:
                    file.write(line)
            else:
                file.write(line)
    
    # Log if no changes were made
    if not changes_made:
        print(f"No changes made to {file_path}")

# Iterate over each file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.yaml'):
        file_path = os.path.join(directory, filename)
        correct_date_format(file_path)

print("Date formats corrected successfully in all .yaml files.")
