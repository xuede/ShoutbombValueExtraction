# Shoutbomb Extraction Script

This Python script is designed to extract library notice counts and the number of registered patrons for each library from a text file and generate a CSV output. It is specifically tailored for internal use at the library.

## Usage

1. Ensure you have Python installed on your system.
2. Place the input text file containing the library data in the same directory as the script. Update the `input_file` variable in the script with the correct file name or path.
3. Run the script using the command: `python Shoutbomb_extraction.py`
4. The script will extract the data from the input file and generate a CSV file with the extracted data. The output file name can be specified by updating the `output_file` variable in the script.

## Input File Format

The input text file should contain the library data in the following format:

​```
Library Name sent for the month, this many text notices = NoticeCount
Library Name has RegisteredPatrons registered patrons for text notices
​```

Example:
​```
Acme Lib (OPP) sent for the month, this many text notices = 19
Rodent Mound Lib (CLP) has 4 registered patrons for text notices
​```

## Output CSV Format

The script generates a CSV file with the following columns:
- Library: The name of the library
- NoticeCount: The count of text notices sent by the library for the month
- RegisteredPatrons: The number of registered patrons for text notices for the library

## Dependencies

This script has no external dependencies and only uses built-in Python modules (`re` and `csv`). Therefore, you don't need to install any additional packages or set up a virtual environment to run the script.

However, let's be honest: who doesn't love using virtual environments? 🙃 If you're a fan of organizing and isolating your projects, feel free to create a virtual environment for this script. It's like having a cozy little home for your code!

## License

This script is released under the MIT License. You are free to use, modify, and distribute the script as needed for internal use at the library. However, please note that the script is provided as-is without any warranty or support.

## Credits

This script was developed by Michael Wargula for internal use by the Electronic Information Network.
