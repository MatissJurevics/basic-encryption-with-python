from cryptography.fernet import Fernet

## function for decryption
def decrypt(dir, key):
    ## reads data from file
    try:
        with open(f'{dir}.txt', 'rb') as f:
            message = f.read()
            f.close()
    except:
        print(f'Error: couldnt read {dir}.txt')
    
    ## uses the key and decrypts the message
    try:
        f = Fernet(key)
        dmessage = str(f.decrypt(message))
    except:
        print('Error: could not decrypt with the provided key')
    ## string contains b' at the beggining and ' at the end so this just cuts that out
    fdmessage = dmessage[2:-1]
    print(fdmessage)

    ## writes the decrypted and formatted message to a text file called 'DecryptedMessage.txt'
    with open('DecyptedMessage.txt' , 'w') as f:
        f.write(fdmessage)
        f.close()


## function to grab a key
def getkey():
    ## looks for key and throws error if not found
    try:
        with open('key.txt', 'rb') as f:
            key = f.read()
            return key
    except:
        print('Error: Key.txt not in Folder')


## gets user to input the name of the encryted file
mdir = input('name of file (decrypt.py must be in the same folder, caseSensitive):\n')
key = getkey()
decrypt(mdir, key)

