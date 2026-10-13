import string

alphabet = list(string.ascii_uppercase)

def vigenere_sq():
    #prints vigenere square
    print(f'|   || A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |') #top row
    print(f'|---||---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|') #divider row
    for letter in alphabet:         #for every letter in the alphabet
        print(f'| {alphabet[0]} ||', end="")     #prints header of each row and forces the next print to keep on the same line
        for i in range(0, 26):              #for each row
            print(f' {alphabet[0]} |', end="")      #prints first object in the list, and forces the next print to keep on the same line
            alphabet.append(alphabet.pop(0))        #move the first object in the list to the back
        print()         #print nothing to change the line
        alphabet.append(alphabet.pop(0))        #move the first object in the list to the back so the header is correct

def letter_to_index(letter, alphabet):
    #returns the letter's integer position in alphabet
    if letter not in alphabet:  #if letter isnt in alphabet list
        return False        #get outta heyuh
    elif letter in alphabet:    #if the letter is in the alphabet list
        return alphabet.index(letter)

def index_to_letter(index, alphabet):
    #returns letter found at position
    if index > 25 or index < 0:     #If index is out of range
        return False        #get outta heyuh
    elif alphabet[index]:       #if index is present in alphabet's index
        return alphabet[index]

def vigenere_encryptor(key, plaintext, alphabet):
    #takes strings and takes them apart, turns each letter into a number, maths each intersection of plaintext and key into a new number, then turns THAT back into a letter to make a new letter
    keyindex = []
    inputindex = []
    encryption = []
    keylist = list(key.replace(" ", ""))      #creates a list from key minus whitespaces
    plaintextlist = list(plaintext.replace(" ", ""))      #creates a list from plaintext input minus whitespaces
    for letter in keylist:      #for each letter in keylist
        keyindex.append(letter_to_index(letter, alphabet))  #puts each letter thru the letter_to_index function and tacks it onto keyindex
    for letter2 in plaintextlist:    #for each letter in plaintext
        inputindex.append(letter_to_index(letter2, alphabet))    #puts each letter thru the letter_to_index function and tacks it onto plainindex
    for num in inputindex:      #for each integer in plainindex
        cipher = (num + keyindex[0]) % 26   #maths with the keyindex
        keyindex.append(keyindex.pop(0))    #then loops the keyindex
        encryption.append(index_to_letter(cipher, alphabet))    #turns math output back into letters and tacks em onto encryption
    output = "".join(encryption)
    print(f'Your encrypted sentence is: {output}')

def vigenere_encryptor_start():
    #starts the process of encryption by taking input from the user and making sure its uppercase for the encryptor to understand
    plaintext = input("What is your message? ").upper()
    key = input("What is your key? ").upper()
    vigenere_encryptor(key, plaintext, alphabet)

def vigenere_decryptor(key, encrypted, alphabet):
    keyindex = []
    inputindex = []
    decrypted = []
    keylist = list(key.replace(" ", ""))  # creates a list from key minus whitespaces
    outputlist = list(encrypted.replace(" ", ""))  # creates a list from output minus whitespaces
    for letter in keylist:  # for every letter in keylist
        keyindex.append(letter_to_index(letter, alphabet))  # puts each letter thru the letter_to_index function and tacks it onto keyindex
    for letter2 in outputlist:  # for every letter in outputlist
        inputindex.append(letter_to_index(letter2, alphabet))  # puts each letter thru the letter_to_index function and tacks it onto outputindex
    for num in inputindex:  # for every number in outputindex
        cipher = (num - keyindex[0] + 26) % 26  # maths with the keyindex
        keyindex.append(keyindex.pop(0))  # then loops through the keyindex
        decrypted.append(index_to_letter(cipher, alphabet))  # turns the math back into letters and appends the result onto encryption
    plaintext = "".join(decrypted)  # when the above loop is done, it puts it all together into one string
    print(f'Your decrypted sentence is: {plaintext}')

def vigenere_decryptor_start():
    ciphertext = input("What is your message? ").upper()
    key = input("What is your key? ").upper()
    vigenere_decryptor(key, ciphertext, alphabet)

def vigenere_start():
    print("Welcome to Sophie's Vigenere Encryptor v2!")
    print("[---]-[---]-[---]")
    print("Didn't change much tbh, i already used list(), join()")
    print("and parsed thru indexes, so i just cleaned it up.")
    print("------")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Both")
    print("4. Exit")
    choice = int(input("Enter here: "))
    if choice == 1:
        vigenere_encryptor_start()
    elif choice == 2:
        vigenere_decryptor_start()
    elif choice == 3:
        vigenere_encryptor_start()
        vigenere_decryptor_start()
    elif choice == 4:
        print("Bye!")
    else:
        print("Please enter a valid option!")


vigenere_sq()
vigenere_start()