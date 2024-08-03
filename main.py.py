def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            shifted_char = ord(char) + shift_amount
            if char.islower():
                if shifted_char > ord('z'):
                    shifted_char -= 26
                encrypted_text += chr(shifted_char)
            elif char.isupper():
                if shifted_char > ord('Z'):
                    shifted_char -= 26
                encrypted_text += chr(shifted_char)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            shifted_char = ord(char) - shift_amount
            if char.islower():
                if shifted_char < ord('a'):
                    shifted_char += 26
                decrypted_text += chr(shifted_char)
            elif char.isupper():
                if shifted_char < ord('A'):
                    shifted_char += 26
                decrypted_text += chr(shifted_char)
        else:
            decrypted_text += char
    return decrypted_text

def main():
    choice = input("Type 'encrypt' to encrypt a message, 'decrypt' to decrypt a message: ").strip().lower()
    if choice not in ['encrypt', 'decrypt']:
        print("Invalid choice! Please type 'encrypt' or 'decrypt'.")
        return
    
    text = input("Enter your message: ")
    shift = int(input("Enter the shift value: "))
    
    if choice == 'encrypt':
        encrypted_message = encrypt(text, shift)
        print(f"Encrypted message: {encrypted_message}")
    elif choice == 'decrypt':
        decrypted_message = decrypt(text, shift)
        print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()
