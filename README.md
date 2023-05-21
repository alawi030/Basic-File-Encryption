# Basic-File-Encryption

The following code represents a File-Encryption program (Ransomware) for educational purposes only. 
It is inspired by a tutorial I watched and serves the purpose of enhancing understanding about encryption concepts.

-------------

# DISCLAIMER

### The ransomware is intended solely for educational purposes and knowledge sharing.
### It is strictly prohibited to utilize this code or any associated techniques to cause harm, engage in illegal activities, or compromise the security and privacy of individuals or systems.

-------------

# What's a Ransomware?

A ransomware is a malicious software that specifically targets and restricts legitimate users from accessing their devices or data.
It operates by demanding a ransom payment in exchange for restoring the normal functionality of the affected system. 
Ransomware has gained prominence as a widespread extortion tool, with the most successful variant being encryption-based ransomware. 
This particular type encrypts the victim's data, and the decryption key is provided only after the ransom is paid to the attacker.

For a ransomware to achieve broad success, it typically needs to satisfy three key conditions:

**Condition 1**: The malicious binary code does not contain any easily accessible secrets, such as decryption keys. In some cases, advanced techniques like white box cryptography are employed to achieve this.

**Condition 2**: The ability to decrypt the compromised device remains solely with the attacker who initiated the ransomware attack.

**Condition 3**: Decrypting one device does not provide any useful information for other infected devices. As a result, the decryption key is not shared among them.
