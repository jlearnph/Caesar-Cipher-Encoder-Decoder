#encrypter
def encrypter (string,steps):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    numbers = '0123456789'
    encrypted = ''
    for i in string:
        if i in alphabet:
            encrypted += alphabet[(alphabet.find(str(i)) + steps) % 26]
        elif i in alphabet.upper():
            encrypted += alphabet[(alphabet.find(str(i.lower())) + steps) % 26].upper()
        elif i in numbers:
            encrypted += numbers[(numbers.find(str(i)) + steps) % 10]
        else:
            encrypted += i
    return encrypted


#decrypter
def decrypter (string, steps = 0):
    if steps != 0:
        return encrypter(string, -int(steps))
    else:
        print('Testing all possible shifts: \n')
        for i in range(1,26):
            decrypted = encrypter(string, -i)
            print('Shift: {} - Message: {}'.format(i,decrypted))


def main ():
    print('''
    This is a caesar cipher message encoder / decoder

    Caesar cipher is one of the simplest and most widely known encryption techniques.
    It is a type of substitution cipher in which each letter in the plaintext is replaced 
    by a letter some fixed number of positions down the alphabet. 

    For example.

    A left shift of 3 means:
    D -> A
    E -> B
    3 -> 0

    A right shift of 5 means:
    G -> L
    Z -> E
    9 -> 4

    *Enter 1 to encode a message
    *Enter 2 to decode a message
    ''')

    while True:
        choice = input('Do you want to encode or decode: ')
        if choice == '1':
            string = input('Enter string that you want to encrypt: ')
            steps = int(input('Enter Shift: '))
            encrypted = encrypter(string,steps)
            print('Encrypted Message: {}'.format(encrypted))
            break
        elif choice == '2':
            string = input('Enter string that you want to decrypt: ')
            ask = input('Do you know the shift? [Y/N]: ')
            if ask == 'Y' or ask == 'y':
                steps = input('Shift: ')
                decrypted = decrypter(string,steps)
                print('Decrypted Message: {}'.format(decrypted))
            else:
                decrypter(string, 0)
            break
        else:
            print('Enter only either 1 or 2')

main()
