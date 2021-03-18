# DNA_cryptography
This program allows you to use the DNA algorithm in cryptography. 

## DNA based Encryption and Decryption Algorithm

    * Use dna_encryption.py to encrypt your message.
    * Use dna_decryption.py to decrypt it.
----------------------------------------------------------------
DNA encryption is a type of substitution encryption as it replaces each character in the message with its DNA equivalent:

<img src="https://media.discordapp.net/attachments/635278809741918218/820718763031920680/dna_codes.png"
     alt="DNA codes"
     style="float: left; margin-right: 10px;" />

> The encryption algorithm has been made with the DNA codon table, A codon table can be used to translate a genetic code into a sequence of amino acids. The standard genetic code is traditionally represented as an RNA codon table, because when proteins are made in a cell by ribosomes, it is messenger RNA that directs protein biosynthesis :

<img style="float: left; margin-right: 10px;" alt="algo" src="https://media.discordapp.net/attachments/779677826865561620/821185136061841458/1bbCyiW35hBU3GiaiF4Qcmw.png" width="600px" height="358px" />

> Symmetric encryption is a type of encryption where only one key (a secret key) is used to both encrypt and decrypt electronic information. The entities communicating via symmetric encryption must exchange the key so that it can be used in the decryption process.

----------------------------------------------------------------
## Usage

```
user$ python3 dna_encryption.py
Input: hello world
Encryption: ACTACAAGTAGTATGCTTGCGATGCACAGTAAT

user$ python3 dna_decryption.py
Input: ACTACAAGTAGTATGCTTGCGATGCACAGTAAT
Decryption: hello world
```

### Note:
This program is inspired by b00t2root19 CTF: Genetics, and <a href="https://www.youtube.com/watch?v=3LwF_LBepOY&t=189s&ab_channel=JohnHammond" target="_blank">John Hammond's writeup</a>

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
