import string

def creat_alphabet_dic():
    result = {}
    alphabet = list(string.ascii_lowercase)
    for letter in alphabet:
        result[letter] = 0
    return result

def is_pangram(s):
    letter_count = creat_alphabet_dic()
    for character in s:
        if character.lower() not in list(string.ascii_lowercase):
            pass
        else:
            letter_count[character.lower()] += 1
    for letter,count in letter_count.items():
        print(letter,count)
        if count == 0:
            return False
    return True
