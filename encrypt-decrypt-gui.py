import tkinter as tk
import random
from cryptography.fernet import Fernet

root = tk.Tk()
root.title("En-Decryptor")

e = tk.Entry(root, width=35, borderwidth=7)
e.grid(row=0, column=0, columnspan=3, padx=0, pady=0)

bt = "Encrypt"
bt2 = "Decrypt"


def encrypt():
    key_file = 'key.key'
    output_file = 'text.encrypted'

    file = open(key_file, 'rb')
    key = file.read()
    file.close()


    message = e.get().encode()

    fernet = Fernet(key)
    encrypted = fernet.encrypt(message)

    with open(output_file, 'wb') as f:
        f.write(encrypted)
        f.close()

def decrypt():
    input_file = 'text.encrypted'
    output_file = 'text.decrypted'
    key_file = 'key.key'

    file = open(key_file, 'rb')
    key = file.read()
    file.close()

    with open(input_file, 'rb') as f:
        data = f.read()  # Read the bytes of the encrypted file

    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)

    with open(output_file, 'wb') as f:
        f.write(decrypted)


button_1 = tk.Button(root, text=bt, padx=40, pady=20, command=encrypt)
button_2 = tk.Button(root, text=bt2, padx=40, pady=20, command=decrypt)

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)


root.mainloop()