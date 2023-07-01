# Baisc File Encryption
## Description
This is a simple file encryption program written in Python. It uses the Fernet module from the cryptography package to encrypt and decrypt files. The program is run from the command line and takes two arguments: the name of the file to be encrypted/decrypted and the name of the file to be created. The program will prompt the user for a password to encrypt the file with. The password is then used to decrypt the file. The program will not run if the file to be created already exists.

## Installation
1. Clone the repository:
```bash
git clone
```
2. Navigate to the project directory:
```bash
cd Basic-File-Encryption
```
3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage
### Encrypting a file
1. Run the program:
```bash
python encrypt.py <file_to_encrypt> <file_to_create>
```
2. Enter a password to encrypt the file with.

### Decrypting a file
1. Run the program:
```bash
python decrypt.py <file_to_decrypt> <file_to_create>
```
2. Enter the password used to encrypt the file.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please create an issue or submit a pull request.

## License
This project is licensed under the [MIT License](Licence.txt).

## Acknowledgements
The Basic File Encryption program was developed using Python and the cryptography package.
