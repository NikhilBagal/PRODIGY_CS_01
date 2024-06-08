def get_cipherletter(new_key, letter):
    #alphabets variable 
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if letter in alpha:
        return alpha[new_key]
    else:
        return letter

def encrypt(key, message):
    message = message.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in message:
        new_key = (alpha.find(letter) + key) % len(alpha)
        result = result + get_cipherletter(new_key, letter)

    return result

def decrypt(key, message):
    message = message.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in message:
        new_key = (alpha.find(letter) - key) % len(alpha)
        result = result + get_cipherletter(new_key, letter)

    return result

def get_Input():
    print("Welcome to caesar cypher program: ")
    print()

    print("Do you want to encrypt or decrypt?")
    user_input = input("E/D: ").lower()
    print()

    if user_input == "e":
        print("Encryption mode selected")
        print()
        key = int(input("Enter the key (1 through 26): "))
        text = input("Enter the text to encrypt: ")
        cipherText = encrypt(key,text)
        print(f'CIPHERTEXT: {cipherText }')

    elif user_input == "d":
        print("Decryption mode selected")
        print()
        key = int(input("Enter the key (1 through 26): "))
        text = input("Enter the text to decrypt: ") 
        plainText = decrypt(key,text)
        print(f'PLAINTEXT: {plainText} ')

    else:
        print("Please select correct mode")

get_Input()