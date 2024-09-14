#  Display the decrypted plaintext.
import string

#an alphabet dictionary that maps the letter to its relative position in the alphabet
#{A: , B: 2, ... Z: 26}
alphabet = {letter: index for index, letter in enumerate(string.ascii_letters, start=0)}

#reverse of above
#{1: A, 2: B, ... 26: Z}
indices = {index: letter for letter, index in alphabet.items()}


# Encryption:
#  Prompt the user to enter plaintext and a key.
#  Use the entered key to perform encryption (e.g., Shift cipher).
#  Display the resulting ciphertext.

def encryption():
    plainText = input("Enter plaintext: ")
    if plainText == "":
        return print("No text inputted.")
    key = int(input("Enter key: "))
    if key == "":
        return print("No key inputted.")
    cipherText = ""
    #enumerate through plaintext and print out the letters in its positions + key shift (relative to the alphabet mapping)

    for letter in plainText:
        
        if letter in alphabet:
            shiftedPosition = (alphabet[letter] + key) % 52  # new position is alphabet position + key; % is for the edge case of letters towards the end so that it can wrap back around
            #Case-follow (QoL)

            #add shifted letter to ciphertext, if upper keep but if lower then make lowercase
            if letter.isupper():
                cipherText += indices[shiftedPosition] 
            else:
                cipherText += indices[shiftedPosition].lower()
        else:
            cipherText += letter # non-alphabet characters edge case

    print("Ciphertext: " + cipherText)

# Decryption:
#  Prompt the user to enter ciphertext and the corresponding key used for encryption.
#  Use the entered k
def decryption():
    #reverse of encryption but instead decrement in the shifted position. 
    cipherText = input("Enter ciphertext: ")
    if cipherText == "":
        return print("No text inputted.")
    key = int(input("Enter key: "))
    if key == "":
        return print("No key inputted.")
    plainText = ""
    #enumerate through plaintext and print out the letters in its positions + key shift (relative to the alphabet mapping)

    for letter in cipherText:
        
        if letter in alphabet:
            shiftedPosition = (alphabet[letter] - key) % 52  # new position is alphabet position + key; % is for the edge case of letters towards the end so that it can wrap back around
            #Case-follow (QoL)

            #add shifted letter to ciphertext, if upper keep but if lower then make lowercase
            if letter.isupper():
                plainText += indices[shiftedPosition] 
            else:
                plainText += indices[shiftedPosition].lower()
        else:
            plainText += letter # non-alphabet characters edge case

    print("Plaintext: " + plainText)



# Brute Force Attack:
#  Prompt the user to enter only the ciphertext (without the key).
#  Implement a brute force attack to try all possible keys (shift values) for a Caesar cipher.
#  Display all the possible plaintext results.

def bruteForceAttack():
    cipherText = input("Enter ciphertext: ")
    if cipherText == "":
        return print("No text inputted.")
    # shift key values are 1-26, but in this case the alphabet dictionary contains both lowercase and uppercase so it will be 1-52(51 keys)
    for key in range(0, 52):
        possiblePlainText = ""

        #decrement key so each key is tried
        for letter in cipherText:
            if letter in alphabet:
                shiftedPosition = (alphabet[letter] + key) % 52  

                if letter.isupper():
                    possiblePlainText += indices[shiftedPosition]
                else:
                    possiblePlainText += indices[shiftedPosition].lower()
            else:
                possiblePlainText += letter  

        print(f"Key {key}: {possiblePlainText}")

    




print("Choose an option: \n1. Encryption \n2. Decryption \n3. Brute Force Attack")
choice = input("Enter your choice (1/2/3): ")



if choice == "1":
    encryption()
elif choice == "2":
    decryption()
else:
    bruteForceAttack()
