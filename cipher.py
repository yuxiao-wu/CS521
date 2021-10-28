import binascii
import csv
import random
from base64 import b64encode

'''
A Set of helper functions.

'''


def binary_to_string(n):
    # Helper function that will return ascii from binary
    # Use this to get the original message from a binary number
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()


def string_to_binary(string):
    # Helper function that will return binary from string
    # Use this to get a number from the message
    return int.from_bytes(string.encode(), 'big')


def binary_to_binary_string(binary):
    # Helper function that will return binary as a bit string from binary
    # Use this to convert the binary number into a string of 0s and 1s.
    # This is needed to generate the appropriate random key
    return bin(binary)[2:]


def binary_string_to_binary(bin_string):
    # Helper function that will return binary from a bit string
    # Use this to convert the random key into a number for calculations
    return int(bin_string, 2)


def get_random_bit():
    # Helper function that will randomly return either 1 or 0 as a string
    # Use this to help generate the random key for the OTP
    return str(random.randint(0, 1))


def read_message():
    # Helper function that will read and process message.txt which will provide a good tessting message
    message = ''
    f = open('message.txt', 'r')
    for line in f:
        message += line.replace('\n', ' ').lower()
    return message


class Cipher:

    def __init__(self):
        # Initialize the suite
        # In part 1 create letter_dict and inverse_dict
        # In part 3 create letter_heuristics and call self.read_csv()
        self.letter_dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7,
                            'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14,
                            'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20,
                            'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25, ' ': 26}
        self.inverse_dict = {v: k for k, v in self.letter_dict.items()}
        self.letter_heuristics = {}
        self.wordlist = []
        self.read_csv()

    def rotate_letter(self, letter, n):
        # Rotate a letter by n and return the new letter
        if n == 0:
            return letter
        else:
            if self.letter_dict.get(letter) + n < 26:
                return self.inverse_dict.get(self.letter_dict.get(letter) + n)
            elif self.letter_dict.get(letter) + n == 26:
                return ' '
            else:
                return self.inverse_dict.get((self.letter_dict.get(letter) + n) % 26 - 1)
        return None

    def encode_caesar(self, message, n):
        # Encode message using rotate_letter on every letter and return the cipher text
        ciphered_text = []
        for letter in message:
            ciphered_text.append(self.rotate_letter(letter, n))
        return ''.join(ciphered_text)

    def decode_caesar(self, cipher_text, n):
        # Decode a cipher text by using rotate_letter the opposite direction and return the original message
        original_message = []
        for letter in cipher_text:
            for pairs in self.letter_dict:
                if letter == self.rotate_letter(pairs, n):
                    original_message.append(pairs)
        return ''.join(original_message)

    def read_csv(self):
        # Read the letter frequency csv and create a heuristic save in a class variable
        file = 'letter_frequencies.csv'
        with open(file, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for line in csv_reader:
                self.letter_heuristics.update({line[0].lower(): float(line[1])})

    def score_string(self, string):
        # Score every letter of a string and return the total
        total_score = 0
        for letter in string:
            total_score += self.letter_heuristics.get(letter)
        return total_score

    def crack_caesar(self, cipher_text):
        # Break a caesar cipher by finding and returning the most probable outcome
        high_score = self.score_string(cipher_text)
        for i in range(1, 27):
            new_text = self.decode_caesar(cipher_text, i)
            text_score = self.score_string(new_text)
            if text_score > high_score:
                high_score = text_score
                final_message = new_text
        return final_message

    def encode_vigenere(self, message, key):
        # Encode message using rotation by key string characters
        ciphered_text = []
        for i in range(len(message)):
            n = self.letter_dict.get(key[i % len(key)])
            ciphered_text.append(self.rotate_letter(message[i], n))
        return ''.join(ciphered_text)

    def decode_vigenere(self, cipher_text, key):
        # Decode ciphertext using rotation by key string characters
        original_message = []
        for i in range(len(cipher_text)):
            n = self.letter_dict.get(key[i % len(key)])
            for pairs in self.letter_dict:
                if cipher_text[i] == self.rotate_letter(pairs, n):
                    original_message.append(pairs)
        return ''.join(original_message)


    def encode_otp(self, message):
        # Similar to a vernan cipher, but we will generate a random key string and return it
        key_list = []
        numeric_message = string_to_binary(message)
        numeric_message_string = binary_to_binary_string(numeric_message)
        for _ in range(len(numeric_message_string)):
            key_list.append(random.randint(0, 1))
        return numeric_message, key_list

    def decode_otp(self, cipher_text, key):
        # XOR cipher text and key. Convert result to string
        return None

    def read_wordlist(self):
        # Extra Credit: Read all words in wordlist and store in list. Remember to strip the endline characters
        filename = "wordlist.txt"

    def crack_vigenere(self, cipher_text):
        # Extra Credit: Break a vigenere cipher by trying common words as passwords
        # Return both the original message and the password used
        self.read_wordlist()
        return None, None


print("---------------------TEST CASES---------------------------")
cipher_suite = Cipher()
print("---------------------PART 1: CAESAR-----------------------")
message = read_message()
cipher_text = cipher_suite.encode_caesar(message, 5)
print('Encrypted Cipher Text:', cipher_text)
decoded_message = cipher_suite.decode_caesar(cipher_text, 5)
print('Decoded Message      :', decoded_message)
print("------------------PART 2: BREAKING CAESAR------------------")
cracked = cipher_suite.crack_caesar(cipher_text)
print('Cracked Code:', cracked)
print("---------------------PART 3: Vignere----------------------")
password = 'dog'
print('Encryption key: ', password)
cipher_text = cipher_suite.encode_vigenere(message, password)
print('Encoded:', cipher_text)
decoded_message = cipher_suite.decode_vigenere(cipher_text, password)
print('Decoded:', decoded_message)

print("-----------------------PART 4: OTP------------------------")

cipher_text, key = cipher_suite.encode_otp(message)
decoded = cipher_suite.decode_otp(cipher_text, key)
print('Cipher Text:', cipher_text)
print('Generated Key:', key)
print('Decoded:', decoded_message)

print('---------PART 5: Breaking Vignere (Extra Credit)----------')
cracked, pwrd = cipher_suite.crack_vigenere(cipher_text)
print('Cracked Code:', cracked)
print('Password:', pwrd)
