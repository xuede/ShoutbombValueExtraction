import re
import csv

def extract_data(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    pattern = r'(\w[\w\s\(\)-.]+)\ssent\sfor\sthe\smonth,\sthis\smany\stext\snotices\s=\s(\d+)'
    matches = re.findall(pattern, content)

    data = []
    for match in matches:
        library_name = match[0].strip()
        notice_count = int(match[1])
        data.append([library_name, notice_count])

    return data

def write_to_csv(data, output_file):
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Library', 'NoticeCount'])
        writer.writerows(data)

# Specify the input text file path
input_file = 'rawdata.txt'  # Update with the correct file name or path

# Specify the output CSV file path
output_file = 'output.csv'  # Update with the desired output file name or path

# Extract the data from the text file
data = extract_data(input_file)

# Write the data to the CSV file
write_to_csv(data, output_file)

print(f"Data has been extracted and saved to {output_file}.")
