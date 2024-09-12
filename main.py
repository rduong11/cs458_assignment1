import string

#an alphabet dictionary that maps the letter to its relative position in the alphabet
#{A: , B: 2, ... Z: 26}
alphabet = {letter: index for index, letter in enumerate(string.ascii_uppercase, start=0)}

#reverse of above
#{1: A, 2: B, ... 26: Z}
indices = {index: letter for letter, index in alphabet.items()}


# Encryption:
#  Prompt the user to enter plaintext and a key.
#  Use the entered key to perform encryption (e.g., Shift cipher).
#  Display the resulting ciphertext.

def encryption():
    plainText = input("Enter plaintext: ").upper()
    key = int(input("Enter key: "))
    cipherText = ""
    #enumerate through plaintext and print out the letters in its positions + key shift (relative to the alphabet mapping)

    for letter in plainText:
        shift = key
        
        if letter in alphabet:
            shiftedPosition = (alphabet[letter] + shift) % 26  # new position is alphabet position + key; % is for the edge case of letters towards the end so that it can wrap back around
            cipherText += indices[shiftedPosition] #add shifted letter to ciphertext

            #Case-follow (QoL)

            # if letter.isupper():
            #     cipherText += shiftedLetter
            # else:
            #     cipherText += shiftedLetter.lower()
        else:
            cipherText += letter # non-alphabet characters edge case

    print("Ciphertext: " + cipherText)

# Decryption:
#  Prompt the user to enter ciphertext and the corresponding key used for encryption.
#  Use the entered key to perform decryption and retrieve the original plaintext.
#  Display the decrypted plaintext.

def decryption():
    #reverse of encryption but instead decrement in the shifted position. 
    cipherText = input("Enter ciphertext: ").upper()
    key = int(input("Enter key: "))
    plainText = ""
    #enumerate through plaintext and print out the letters in its positions + key shift (relative to the alphabet mapping)

    for letter in cipherText:
        shift = key
        
        if letter in alphabet:
            shiftedPosition = (alphabet[letter] - shift) % 26  # new position is alphabet position - key; the % is for the edge case of letters towards the end so that it can wrap back around
            plainText += indices[shiftedPosition] #add shifted letter to ciphertext

            #Case-follow (QoL)

            # if letter.isupper():
            #     cipherText += shiftedLetter
            # else:
            #     cipherText += shiftedLetter.lower()
        else:
            plainText += letter # non-alphabet characters edge case

    print("Ciphertext: " + plainText)



# Brute Force Attack:
#  Prompt the user to enter only the ciphertext (without the key).
#  Implement a brute force attack to try all possible keys (shift values) for a Caesar cipher.
#  Display all the possible plaintext results.

def bruteForceAttack():
    pass




print("Choose an option: \n1. Encryption \n2. Decryption \n3. Brute Force Attack")
choice = input("Enter your choice (1/2/3): ")



if choice == "1":
    encryption()
elif choice == "2":
    decryption()
else:
    bruteForceAttack()
