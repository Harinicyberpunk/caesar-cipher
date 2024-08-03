# Caesar Cipher Encryptor and Decryptor

This Python script implements a basic Caesar cipher for encrypting and decrypting text. The Caesar cipher is a type of substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet. This script provides a simple interface for users to either encrypt or decrypt messages by specifying the shift value.

## Features

- Encrypt a message by shifting characters.
- Decrypt a message by reversing the shift of characters.
- Handles both uppercase and lowercase letters.
- Retains non-alphabetic characters unchanged.

## Usage

1. Clone the repository or download the script.
2. Run the script using Python.
3. Follow the on-screen prompts to either encrypt or decrypt a message.

## Code Explanation

### Functions

1. **encrypt(text, shift)**:
    - Encrypts the given `text` by shifting characters by the specified `shift` amount.
    - Handles both uppercase and lowercase letters.
    - Non-alphabetic characters are retained as is.

2. **decrypt(text, shift)**:
    - Decrypts the given `text` by reversing the shift of characters by the specified `shift` amount.
    - Handles both uppercase and lowercase letters.
    - Non-alphabetic characters are retained as is.

3. **main()**:
    - Prompts the user to choose between encryption and decryption.
    - Prompts the user to enter the message and shift value.
    - Displays the encrypted or decrypted message based on the user's choice.

### Running the Script

To run the script, execute the following command in your terminal or command prompt:

```sh
python caesar_cipher.py
```

Follow the on-screen instructions to encrypt or decrypt a message.

### Example

```sh
Type 'encrypt' to encrypt a message, 'decrypt' to decrypt a message: encrypt
Enter your message: Hello World!
Enter the shift value: 3
Encrypted message: Khoor Zruog!
```

## License

This project is licensed under the MIT License.

## Author

Harini

## Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## Acknowledgements

Inspired by classical cryptography techniques.

---

This `README` file provides an overview of the script, its features, usage instructions, and other relevant information for users and contributors.
