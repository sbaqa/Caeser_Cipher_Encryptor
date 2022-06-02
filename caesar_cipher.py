from helper import logo
from helper import alphabet
from helper import encrypt, decrypt

# Check user's input choice
def call_caesar_cipher(action, message, action_num):
  if action_num > len(alphabet):
    action_num = action_num % 26
  if action == "encode":
    encrypt(plain_text=message, shift_amount=action_num)
  elif action == "decode":
    decrypt(plain_text=message, shift_amount=action_num)
  else:
    print("Wrong action input, please type 'encode' or 'decode' in CLI to run the program properly...")

# Run program, receive input and check if user wants restart program
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
