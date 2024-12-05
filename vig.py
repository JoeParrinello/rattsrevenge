from itertools import product
from string import ascii_uppercase
import re
pattern = re.compile("[AEIOU]")
def is_good_key(x):
  return len(x) >=2 and len(x) <=8

def generate_key(msg, key):
    key = list(key)
    if len(msg) == len(key):
        return "".join(key)
    else:
        for i in range(len(msg) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def load_words():
    with open('all_english_words.txt') as word_file:
        valid_words = set(map(str.upper, filter(is_good_key, word_file.read().split())))

    return valid_words

def decrypt_vigenere(msg, word):
    key = generate_key(msg, word)
    decrypted_text = []
    for i in range(len(msg)):
        char = msg[i]
        decrypted_char = chr((ord(char) - ord(key[i]) + 26) % 26 + ord('A'))
        decrypted_text.append(decrypted_char)
    decrypt_word = "".join(decrypted_text)
    if bool(pattern.search(decrypt_word)):
        return f"Keyword: {word:8}, Decrypt: {decrypt_word}\n"
    else:
        return None

cipher = "JYPFFQVY"
with open("output.txt", "w") as f: 
    for i in load_words():
        decrypted = decrypt_vigenere(cipher, i)
        if decrypted is not None:
            f.write(decrypted)


