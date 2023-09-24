from collections import Counter
from pathlib import Path

def count_letters(text):
    combined_text = ''.join(text)
    return dict(Counter(char.lower() for char in combined_text if char.isalpha()))

def sort_letters(letters):
    return sorted([(letter, count) for letter, count in letters.items()],
                  key=lambda x: int(x[1]), reverse=True)

def output_report(path, count, letters):
    print('\n'.join([
    f"--- Begin report of {path} ---",
    f"{count} words found in the document",
    "",
    * [f"The '{letter[0]}' character was found {letter[1]} times" for letter in letters],
    "",
    "--- End report ---"
    ]))

def analyze_text(path):
    with open(path) as f:
        text = f.read().split()
        file_name = Path(path).name
        if len(text):
            output_report(file_name, len(text), sort_letters(count_letters(text)))

analyze_text(Path(input("Enter path to text:")))
