def encrypt(message, key):
    encrypted_message = ""
    mapping = {}  # To store character mappings for explanation

    for char in message:
        if char.isalpha():
            original_char = char
            shifted = ord(char) + key
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
            encrypted_char = chr(shifted)
            mapping[original_char] = encrypted_char
            encrypted_message += encrypted_char
        else:
            print(f"Invalid character '{char}' in the message. Only alphabetic characters are allowed.")

    print("\nMapping of characters:")
    for original_char, encrypted_char in mapping.items():
        print(f"{original_char} ---> {encrypted_char}")

    return encrypted_message

def decrypt(message, key):
    decrypted_message = ""
    mapping = {}  # To store character mappings for explanation

    for char in message:
        if char.isalpha():
            original_char = char
            shifted = ord(char) - key
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
            decrypted_char = chr(shifted)
            mapping[original_char] = decrypted_char
            decrypted_message += decrypted_char
        else:
            print(f"Invalid character '{char}' in the message. Only alphabetic characters are allowed.")

    print("\nMapping of characters:")
    for original_char, decrypted_char in mapping.items():
        print(f"{original_char} ---> {decrypted_char}")

    return decrypted_message


def main():
    while True:
        print("\nChoose an operation:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            message = input("\nEnter the message: ")
            key = int(input("Enter the key: "))
            encrypted_message = encrypt(message, key)
            print(f"\nEncrypted message: {encrypted_message}")

        elif choice == '2':
            message = input("\nEnter the message: ")
            key = int(input("Enter the key: "))
            decrypted_message = decrypt(message, key)
            print(f"\nDecrypted message: {decrypted_message}")

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
