decrypted=b"abcdefghijklmnopqrstuvwxyz"
encrypted=b"qwertyuiopasdfghjklzxcvbnm"
encrypt_table=bytes.maketrans(decrypted,encrypted)
decrypt_table=bytes.maketrans(encrypted,decrypted)
answer=''
choice=''
message=''
while choice !='0':
    choice=input("Do you want to encrypt or decrypt the message???\nPress 1 to Encrypt..... Press 2 to Decrypt or Press 0 to exit the program.....\n")

    if choice=='1':
        message=input('\nEnter your message for encryption: ')
        answer=message.translate(encrypt_table)
        print(answer + '\n\n')

    elif choice=='2':
        message=input('\nEnter your message for encryption: ')
        answer=message.translate(decrypt_table)
        print(answer + '\n\n')

    elif choice !='0':
        print('You have entered wrong input..... Please try again. \n\n')
