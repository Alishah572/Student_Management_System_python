from random import shuffle
from string import punctuation, digits, ascii_letters

def get_chars():
    # Helper to ensure consistent character set
    return list(" " + punctuation + digits + ascii_letters)

def generate_key():
    chars = get_chars()
    key = chars.copy()
    shuffle(key)
    return chars, key

def encrypt_message(plain_text, chars, key):
    cipher_text = ""
    for letter in plain_text:
        if letter in chars:
            index = chars.index(letter)
            cipher_text += key[index]
        else:
            cipher_text += letter
    return cipher_text

def decrypt_message(cipher_text, chars, key):
    plain_text = ""
    for letter in cipher_text:
        if letter in key:
            index = key.index(letter)
            plain_text += chars[index]
        else:
            plain_text += letter
    return plain_text