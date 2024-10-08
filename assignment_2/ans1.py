def is_consonant(char):
    if char.isalpha() and char.lower() not in "aeiou":
        return True
    else:
        return False

def get_count(a_string):
    count_number = 0
    for char in a_string:
        if is_consonant(char):
            count_number += 1
    return count_number


def main():
    text = "Hello, World!"
    consonant_count = get_count(text)
    print(consonant_count)

main()