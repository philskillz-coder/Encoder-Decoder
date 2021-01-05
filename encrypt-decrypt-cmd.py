from cryptography.fernet import Fernet

key_file = 'key.key'
input_file = 'text.txt'
output_file = 'text.encrypted'

input_file2 = 'text.encrypted'
output_file2 = 'text.decrypted'

file = open(key_file, 'rb')
key = file.read()
file.close()

cmd = input("encrypt or decrypt? ")
if cmd == 'encrypt':
    message_input = input("Enter a text to encrypt: ")

    message = message_input.encode()

    fernet = Fernet(key)
    encrypted = fernet.encrypt(message)

    with open(output_file, 'wb') as f:
        f.write(encrypted)
        f.close()
    print("Encrypted.")

if cmd == 'decrypt':
    with open(input_file2, 'rb') as f:
        data = f.read()  # Read the bytes of the encrypted file

    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)

    with open(output_file2, 'wb') as f:
        f.write(decrypted)

    print("Decrypted.")
else:
    exit()