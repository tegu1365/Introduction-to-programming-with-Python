def add13(letter):
    new_symbol = chr(ord(letter) + 13)
    if new_symbol > 'z':
        diff = ord(new_symbol) - ord('z')
        new_symbol = chr(ord('a') + diff - 1)
    return new_symbol


def rot_13(message):
    result = ""
    for symbol in message:
        if 'a' <= symbol <= 'z':
            new_symbol = add13(symbol)
        elif 'A' <= symbol <= 'Z':
            new_symbol = add13(symbol.lower()).upper()
        else:
            new_symbol = symbol
        result += new_symbol
    return result


def atbash(message):
    key_table = {'A': 'Z',
                 'B': 'Y',
                 'C': 'X',
                 'D': 'W',
                 'E': 'V',
                 'F': 'U',
                 'G': 'T',
                 'H': 'S',
                 'I': 'R',
                 'J': 'Q',
                 'K': 'P',
                 'L': 'O',
                 'M': 'N',
                 'N': 'M',
                 'O': 'L',
                 'P': 'K',
                 'Q': 'J',
                 'R': 'I',
                 'S': 'H',
                 'T': 'G',
                 'U': 'F',
                 'V': 'E',
                 'W': 'D',
                 'X': 'C',
                 'Y': 'B',
                 'Z': 'A'}

    result = ""
    for symbol in message:
        if 'a' <= symbol <= 'z':
            new_symbol = key_table[symbol.upper()].lower()
        elif 'A' <= symbol <= 'Z':
            new_symbol = key_table[symbol]
        else:
            new_symbol = symbol
        result += new_symbol
    return result


def fn_xor(message):
    xor_key = '62538'
    result = ""
    i = 0
    for symbol in message:
        # print(f" {symbol} xor {xor_key[i]} is {ord(symbol) ^ ord(xor_key[i])}")
        new_symbol = chr(ord(symbol) ^ ord(xor_key[i]))
        result += new_symbol
        i += 1
        if i >= len(xor_key):
            i = 0
    return result


def encrypt_message(type_of_encrytion):
    def decorator(func):
        def encryption(*arg, **kwargs):
            if type_of_encrytion == 'ROT-13':
                # print('rot-13 encrypt: ')
                return rot_13(func(*arg, **kwargs))
            elif type_of_encrytion == 'ATBASH':
                # print('atbash encrypt: ')
                return atbash(func(*arg, **kwargs))
            elif type_of_encrytion == 'FN-XOR':
                # print('fn-xor encrypt: ')
                return fn_xor(func(*arg, **kwargs))

        return encryption

    return decorator


@encrypt_message('ROT-13')
def michael_bolton():
    return 'This is the tale of Captain Jack Sparrow!'


print(michael_bolton())  # Guvf vf gur gnyr bs Pncgnva Wnpx Fcneebj!


@encrypt_message('ATBASH')
def michael_bolton(person):
    return f'This is the tale of {person}!'


print(michael_bolton('Captain Jack Sparrow'))  # Gsrh rh gsv gzov lu Xzkgzrm Qzxp Hkziild!


@encrypt_message('FN-XOR')
def michael_bolton(person, description):
    return f'This is the tale of {person}, {description}!'


print(michael_bolton('Captain Jack Sparrow',
                     'pirate so brave of the Seven Seas'))  # bYZC_BDYSGQ]S\VuPCDP__zPUZcAWCA_FCYCWEVBYQBP@T_WE[UeTEU_bVQB

# print(rot_13("AaB"))
# print(atbash("AaB"))
# print(fn_xor('Cryptography'))
