from collections import defaultdict
import sys

def get_lexicon(file_path):
    '''A function that takes one parameter (a string representing a file path)
    and returns the lines of the file in a list. '''
    with open(file_path, 'r') as file:
        lines = file.readlines()
        lines_cleaned = [line.strip() for line in lines]
    return lines_cleaned

def get_sorted(raw_list):
    '''A function that takes one parameter (a list) and returns the
    list sorted in ascending order. '''
    ascending_list = sorted(raw_list)
    return ascending_list

def get_dict(string_list):
    '''A function that takes one parameter (a list of strings) and
    returns a dictionary where the keys are alphabetically sorted
    versions of the strings, and the values are lists of strings with
    the same characters.'''
    anagram_dict = defaultdict(list)
    for word in string_list:
        # set the key for the dict
        sorted_word = ''.join(sorted(word))
        # set the value for the dict
        anagram_dict[sorted_word].append(word)
    return dict(anagram_dict)

def find_anagrams(anagram_dict, input_word):
    '''A function that takes two parameters (the sorted word dictionary 
    and a user input word from sys) and returns a list of the
    anagrams, not including the user input word'''

    # get user input word in sorted order
    sorted_user_word = ''.join(sorted(input_word))
    anagrams_list = []
    # check this word in the anagram_dict
    if sorted_user_word in anagram_dict:
        for word in anagram_dict[sorted_user_word]:
            if word != input_word:
                anagrams_list.append(word)
        return anagrams_list
    else:
        return []

def main():
    '''A function that takes no parameters and coordinates reading
    the lexicon, building the dictionary, and finding anagrams. Here
    is the only place you should have print statements.'''
    lexicon_list = get_lexicon('sv-utf8.txt')
    sorted_lexicon_list = get_sorted(lexicon_list)
    sorted_lexicon_dict = get_dict(sorted_lexicon_list)
    user_input_word = sys.argv[1]
    answer = find_anagrams(sorted_lexicon_dict, user_input_word)
    print(answer)

if __name__ == '__main__':
    main()
