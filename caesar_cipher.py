from helper import logo
from helper import alphabet

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
  for char in plain_text:
    if char in alphabet:
      alph_position = alphabet.index(char)
      shifted_position = alph_position - shift_amount
      decoded_text += alphabet[shifted_position]
    else:
      decoded_text += char
  print(f"The decoded text is {decoded_text}")


#Program run depending to user's input choice
def call_caesar_cipher(action, message, action_num):
  if action_num > len(alphabet):
    action_num = action_num % 26
  if action == "encode":
    encrypt(plain_text=message, shift_amount=action_num)
  elif action == "decode":
    decrypt(plain_text=message, shift_amount=action_num)
  else:
    print("Wrong action input, please type 'encode' or 'decode' in CLI to run the program properly...")

def run_program():
  print(logo)
  run_again = True
  while run_again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    call_caesar_cipher(direction, text, shift)
    restart_program = input("Do you want to restart the program? Type 'yes' or 'no' please...\n").lower()
    if restart_program == "no":
      run_again = False
      print("Goodbye!")

run_program()
