import string

def create_alphabet_dic():
    result = {}
    alphabet = list(string.ascii_lowercase)
    position = 1
    for letter in alphabet:
        result[letter] = position
        position += 1
    return result


def alphabet_position(text):
    text = text.lower()
    result = ""
    position_dic = create_alphabet_dic()
    for letter in text:
        if letter in list(string.ascii_lowercase):
            result += f"{position_dic[letter]} "
    return result[:-1]
