import csv
import sys

#define global variable
CORRECT_COLOR = "\033[92m" #green
INCORRECT_COLOR = "\033[91m" #red
RESET_COLOR = "\033[0m" #reset color

def load_words(file_path):
    # load words pairs from csv file
    words = {}
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 2:
                #dictionary to store word pair, engish is the key and swedish is the value
                words[row[0].strip()] = row[1].strip()
    return words

def test_user(words):
    # doing the word test and count the correct words that user input
    correct_count = 0
    incorrect_count = 0
    for english, swedish in words.items():
        answer = input(f"What is the correct Swedish translation for '{english}'?")
        if answer.strip().lower() == swedish.lower():
            print(f"{CORRECT_COLOR}Correct answer!{RESET_COLOR}")
            correct_count += 1
        else:
            print(f"{INCORRECT_COLOR}Incorrect!{RESET_COLOR}")
            incorrect_count += 1
    return correct_count, incorrect_count

def main():
    if len(sys.argv) != 2:
        print("Usage: python ans2.py <path_to_csv_file>")
        return
    
    file_path = sys.argv[1]
    words = load_words(file_path)
    while True:
        correct, incorrect = test_user(words)
        print(f"The total score you got is {correct} correct and {incorrect} incorrect.")
        try_again = input("Do you want to try again? (yes/no)").strip().lower()
        if try_again != 'yes':
            break

if __name__ == "__main__":
    main()