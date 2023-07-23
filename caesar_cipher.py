'''
The Caesar cipher is an ancient encryption algorithm used by Julius Caesar. It 
encrypts letters by shifting them over by a 
certain number of places in the alphabet. We 
call the length of shift the key. For example, if the 
key is 3, then A becomes D, B becomes E, C becomes 
F, and so on. To decrypt the message, you must shift 
the encrypted letters in the opposite direction. This 
program lets the user encrypt and decrypt messages 
according to this algorithm.

When you run the code, the output will look like this:

Do you want to (e)ncrypt or (d)ecrypt?
> e
Please enter the key (0 to 25) to use.
> 4
Enter the message to encrypt.
> Meet me by the rose bushes tonight.
QIIX QI FC XLI VSWI FYWLIW XSRMKLX.


Do you want to (e)ncrypt or (d)ecrypt?
> d
Please enter the key (0 to 26) to use.
> 4
Enter the message to decrypt.
> QIIX QI FC XLI VSWI FYWLIW XSRMKLX.
MEET ME BY THE ROSE BUSHES TONIGHT.
'''



SPECIAL_CHARACTERS = {' ', '.', '_', '-'}
THE_ALPHA_BET = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]


def encrypt(input_str: str, key: int) -> str:
    input_str = input_str.lower()
    output_str = ''
    for char in input_str:
        if char in SPECIAL_CHARACTERS:
            output_str += char
            continue
        char_index = THE_ALPHA_BET.index(char)
        index_of_new_char = char_index + key
        if index_of_new_char > len(THE_ALPHA_BET) - 1:
            index_of_new_char = index_of_new_char % (len(THE_ALPHA_BET) - 1)
            index_of_new_char -= 1  # to account for index of list starting at 0
        output_str += THE_ALPHA_BET[index_of_new_char]
    return output_str.upper()


def decrypt(input_str: str, key: int) -> str:
    input_str = input_str.lower()
    output_str = ''
    for char in input_str:
        if char in SPECIAL_CHARACTERS:
            output_str += char
            continue
        char_index = THE_ALPHA_BET.index(char)
        index_of_new_char = char_index - key
        output_str += THE_ALPHA_BET[index_of_new_char]
    return output_str.upper()
