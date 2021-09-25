from cryptography.fernet import Fernet

## generates the encryton key and that
key = Fernet.generate_key()
i = Fernet(key)

## user inputs a message
message = input('Message:\n')
print('your message is:\n'+message)
pause =input('press enter to continue...')

## messageb turns the message into bytes, token is the encrypted messsage
messageb = bytes(message, 'utf8')
token = i.encrypt(messageb)
## user inputs the name of the encrypted file
mes_file_name = input('filename:')

## writes message to a file
with open(f'{mes_file_name}.txt', 'wb') as f:
    f.write(token)
    f.close()
## writes key to a file
with open('key.txt', 'wb') as f:
    f.write(key)
    f.close()