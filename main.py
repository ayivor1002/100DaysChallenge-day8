#import art
from art import game

alphabet = [
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
  'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
  'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
  't', 'u', 'v', 'w', 'x', 'y', 'z'
]

print(game)


def ceaser(text, shift, direction):
  sorting_text = ""
  for char in text:
    if char not in alphabet:
      sorting_text += char
    else:
      position = alphabet.index(char)
      if direction == "encode":
        new_position = position + shift
      elif direction == "decode":
        new_position = position - shift
      else:
        print("No corresponding instruction!")

      new_letter = alphabet[new_position]

      sorting_text += new_letter
  print(f"Resultat: {sorting_text}")


should_continue = True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift %= 26

  ceaser(text, shift, direction)

  restart_a = input("Do you want to restart? type yes or no: ")
  if restart_a == "no":
    should_continue = False
    print("GoodBye...")
