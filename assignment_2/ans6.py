from math import sqrt
from collections import defaultdict

def get_lines(file_path):
    # should take one parameter: the path to a .txt-file. It should return the lines from the file using .readlines().
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        lines_cleaned = [line.strip().replace('!', '').replace(',', '').replace('-','').replace('.', '').replace('"', '') for line in lines]
        return lines_cleaned
    except FileNotFoundError:
        print(f"The file {file_path} does not exist")
        return None

def get_lexicon(file_path):
    # should take one parameter: the path to sv-utf8.txt, which in this case will be only sv-utf8.txt (not the full path). It should
    # return a list of the words in the lexicon sv-utf8.txt
    return get_lines(file_path)

def is_vowel(x):
    # should take one parameter: a single character. It should return True if the character is a vowel and False otherwise.
    return x in "aeiouyåäö"

def get_vowel_count(word):
    # should take one parameter: a word as a string. It should return the number of vowels in the word.
    count = 0
    for char in word:
        if is_vowel(char):
            count += 1
    return count

def get_word_vowels(words):
    # should take one parameter: a list of words. It should
    # return a dictionary where the keys are words, and the values are the number of vowels in each word.
    word_vowel_count = {}
    for word in words:
        word_vowel_count[word] = get_vowel_count(word)
    return word_vowel_count

def get_token_vowels(text_list,vowel_count_dict):
    # should take two parameters: a list of text string and a dictionary mapping words to vowel counts. The function should return
    # a list of vowel counts corresponding to the tokens in the input list.
    token_vowel_counts = []
    for word in text_list:
        token_vowel_counts.append(vowel_count_dict.get(word, 0))
    return token_vowel_counts

def get_mean(numbers):
    if not numbers:
        return 0
    total = sum(numbers)
    count = len(numbers)
    mean = total / count
    return mean

def get_stdev(numbers):
    if not numbers or len(numbers) == 1:
        return 0 
    mean = get_mean(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / (len(numbers) - 1) # Sample variance
    stdev = sqrt(variance)
    return stdev

def main():
   lexicon = get_lexicon('sv-utf8.txt') # read lexicon from sv-utf8.txt
   word_vowel_counts = get_word_vowels(lexicon) # get vowel counts dict for the lexicon
   sentences = get_lines('swe-sentences.txt') # read sentences from txt file 
   #print(sentences) 
   token_vowel_counts = [] # tokenize sentences into words & get vowel counts for the token
   for sentence in sentences:
       words_in_sentence = sentence.split()
       #print(words_in_sentence) 
       token_counts = get_token_vowels(words_in_sentence, word_vowel_counts)
       token_vowel_counts.extend(token_counts)
   # Calculate mean and stdev  
   stdev_vowel_count = get_stdev(token_vowel_counts)
   mean_vowel_count = get_mean(token_vowel_counts)

   print("Mean:", mean_vowel_count)
   print("stdev:", stdev_vowel_count)

if __name__ == "__main__":
    main()