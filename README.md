# Shoutbomb Extraction Script

This Python script is designed to extract library notice counts and the number of registered patrons for each library from a text file and generate a CSV output. It is tailored explicitly for internal use at the Electronic Information Network.

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

But go ahead and venv if you like.

## Roadmap

- [x] Extract notice counts and registered patrons from the input file
- [x] Generate a CSV output with the extracted data
- [ ] Add the ability to dump the entire raw data instead of only the desired output

## Wishlist??
- [ ] Add more statistical data
- [ ] Add data visualization

## License

This script is released under the MIT License. You are free to use, modify, and distribute the script as needed for internal use at the library. However, please note that the script is provided as-is without any warranty or support.

## Credits

This script was developed by Michael Wargula for internal use by the Electronic Information Network.
