from ui_view import logo
from ui_view import alphabet

#Encrypt your message
def encrypt(plain_text, shift_amount):
  encoded_text = ""
  for letter in plain_text:
    alph_position = alphabet.index(letter)
    shifted_position = alph_position + shift_amount
    encoded_text += alphabet[shifted_position]
  print(f"The encoded text is {encoded_text}")

#Decrypt your message
def decrypt(plain_text, shift_amount):
  decoded_text = ""
  for letter in plain_text:
    if letter not in alphabet:
      break
      print("Wrong input!")
    alph_position = alphabet.index(letter)
    shifted_position = alph_position - shift_amount
    decoded_text += alphabet[shifted_position]
  print(f"The decoded text is {decoded_text}")

#Program run depending to user's input choice
def call_caesar_cipher():
  print(logo)
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  if shift > len(alphabet):
    shift = shift % 26
  if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
  elif direction == "decode":
    decrypt(plain_text=text, shift_amount=shift)
  else:
    print("Wrong action input, please type 'encode' or 'decode' in CLI to run the program properly...")

call_caesar_cipher()
