import string

#an alphabet dictionary that maps the letter to its relative position in the alphabet
alphabet = {letter: index for index, letter in enumerate(string.ascii_uppercase, start=1)}

# Encryption:
#  Prompt the user to enter plaintext and a key.
#  Use the entered key to perform encryption (e.g., Shift cipher).
#  Display the resulting ciphertext.

def encryption():
    plainText = input("Enter plaintext:")
    #sajid
    key = input("Enter key: ")
    #1

    #enumerate through plaintext and print out the letters in its positions + 1 (relative to the alphabet mapping)



    print("Ciphertext: ")

# Decryption:
#  Prompt the user to enter ciphertext and the corresponding key used for encryption.
#  Use the entered key to perform decryption and retrieve the original plaintext.
#  Display the decrypted plaintext.

def decryption():
    pass



# Brute Force Attack:
#  Prompt the user to enter only the ciphertext (without the key).
#  Implement a brute force attack to try all possible keys (shift values) for a Caesar cipher.
#  Display all the possible plaintext results.

def bruteForceAttack():
    pass




print("Choose an option: \n1. Encryption \n2. Decryption \n3. Brute Force Attack")
choice = input("Enter your choice (1/2/3): ")



if choice == 1:
    encryption()
elif choice == 2:
    decryption()
else:
    bruteForceAttack()
