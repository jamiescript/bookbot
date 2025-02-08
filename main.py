def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    text = text.lower()
    char_count = {}

    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1



    return char_count

def count_letters(text):
    text = text.lower()
    letter_count = {}

    for char in text:
        if char.isalpha():
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1

    return letter_count

def output(char_count):
    for char, count in char_count.items():
        print(f'The \'{char}\' character was found {count} times')

with open('./books/frankenstein.txt') as f:
    text = f.read()
    print('--- Begin report of books/frankenstein.txt ---')
    print(f'{count_words(text)} words found in document')
    print(output(count_letters(text)))

