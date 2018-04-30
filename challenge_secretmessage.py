import sys
from string import ascii_lowercase

alphabet = ascii_lowercase
newMessage = ""

choice = input("Encrypt or decrypt? ")
# Check if options are valid, otherwise raise an error
if choice == "encrypt" or choice == "decrypt":
    pass
else:
    raise ValueError("Not an option")
message = input("Please enter a message: ")
# Check if key is a positive integer, otherwise raise an error
try:
    key = int(input("Encryption Key: "))
    if key < 0:
        sys.exit()
except:
    raise ValueError("Not a positive integer")

for character in message:
    '''
    Iterate through every character in message, find new letter position
    using Caesar cipher, then add it to the new message.
    '''
    if character in alphabet:
        position = alphabet.find(character)
        if choice == "encrypt":
            newPosition = (position + key) % 26
        elif choice == "decrypt":
            newPosition = (position - key) % 26
        newCharacter = alphabet[newPosition]
        newMessage += newCharacter
    else:
        newMessage += character
print("The new message is:", newMessage)