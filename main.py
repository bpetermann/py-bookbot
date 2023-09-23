from pathlib import Path

def count_words(text):
    words_count = 0
    for _ in text:
        words_count += 1
    return words_count

def count_letters(text):
    letters_dict = {}
    for word in text:
        for char in word:
            index = char.lower()
            if index in letters_dict:
                letters_dict[index] += 1
            elif index.isalpha():
                letters_dict[index] = 1
    return letters_dict

def sort_letters(letters):
    letters_list = []
    for letter in letters:
        letters_list.append((letter, letters[letter]))
    letters_list.sort(key=lambda x:int(x[1]), reverse=True)
    return letters_list

def print_report(count, letters):
    print("--- Begin report ---")
    print(f"{count} words found in the document")
    print("")
    for letter in letters:
        print(f"The '{letter[0]}' character was found {letter[1]} times")
    
    print("")
    print("--- End report ---")

def start_report(path):
    with open(path) as f:
        file_content = f.read()
        text = file_content.split()
        word_count = count_words(text)
        sorted_letters = sort_letters(count_letters(text))

        print_report(word_count, sorted_letters)

data_folder = input("Enter path to text:")
text_file = Path(data_folder)
start_report(text_file)
