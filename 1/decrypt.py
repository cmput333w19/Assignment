#xxd ciphertext1
map = [[0x8, 0x9, 0xb, 0xa, 0xe, 0xf, 0xd, 0xc, 0x4, 0x5, 0x7, 0x6, 0x2, 0x3, 0x1, 0x0 ],   
                [0x9, 0xb, 0xa, 0xe, 0xf, 0xd, 0xc, 0x4, 0x5, 0x7, 0x6, 0x2, 0x3, 0x1, 0x0, 0x8 ],   
                [0x1, 0x0, 0x8, 0x9, 0xb, 0xa, 0xe, 0xf, 0xd, 0xc, 0x4, 0x5, 0x7, 0x6, 0x2, 0x3 ],  
                [0xa, 0xe, 0xf, 0xd, 0xc, 0x4, 0x5, 0x7, 0x6, 0x2, 0x3, 0x1, 0x0, 0x8, 0x9, 0xb ],  
                [0xe, 0xf, 0xd, 0xc, 0x4, 0x5, 0x7, 0x6, 0x2, 0x3, 0x1, 0x0, 0x8, 0x9, 0xb, 0xa ],   
                [0x7, 0x6, 0x2, 0x3, 0x1, 0x0, 0x8, 0x9, 0xb, 0xa, 0xe, 0xf, 0xd, 0xc, 0x4, 0x5 ],    
                [0xd, 0xc, 0x4, 0x5, 0x7, 0x6, 0x2, 0x3, 0x1, 0x0, 0x8, 0x9, 0xb, 0xa, 0xe, 0xf ],  
                [0xc, 0x4, 0x5, 0x7, 0x6, 0x2, 0x3, 0x1, 0x0, 0x8, 0x9, 0xb, 0xa, 0xe, 0xf, 0xd ],  
                [0x4, 0x5, 0x7, 0x6, 0x2, 0x3, 0x1, 0x0, 0x8, 0x9, 0xb, 0xa, 0xe, 0xf, 0xd, 0xc ],    
                [0x5, 0x7, 0x6, 0x2, 0x3, 0x1, 0x0, 0x8, 0x9, 0xb, 0xa, 0xe, 0xf, 0xd, 0xc, 0x4 ],   
                [0xf, 0xd, 0xc, 0x4, 0x5, 0x7, 0x6, 0x2, 0x3, 0x1, 0x0, 0x8, 0x9, 0xb, 0xa, 0xe ],   
                [0x6, 0x2, 0x3, 0x1, 0x0, 0x8, 0x9, 0xb, 0xa, 0xe, 0xf, 0xd, 0xc, 0x4, 0x5, 0x7 ],   
                [0x2, 0x3, 0x1, 0x0, 0x8, 0x9, 0xb, 0xa, 0xe, 0xf, 0xd, 0xc, 0x4, 0x5, 0x7, 0x6 ],    
                [0x3, 0x1, 0x0, 0x8, 0x9, 0xb, 0xa, 0xe, 0xf, 0xd, 0xc, 0x4, 0x5, 0x7, 0x6, 0x2 ],   
                [0xb, 0xa, 0xe, 0xf, 0xd, 0xc, 0x4, 0x5, 0x7, 0x6, 0x2, 0x3, 0x1, 0x0, 0x8, 0x9 ],   
                [0x0, 0x8, 0x9, 0xb, 0xa, 0xe, 0xf, 0xd, 0xc, 0x4, 0x5, 0x7, 0x6, 0x2, 0x3, 0x1 ]]

def split_digit(number):
    digit1 = number//16
    digit2 = number%16
    return hex(digit1),hex(digit2)

def combine_digit(digit1,digit2):
    return hex(digit1*16+digit2)



def given_plaintext_ciphertext_find_key(plain_text,cipher_text):
    ph,pl = split_digit(int(plain_text))
    ch,cl = split_digit(int(cipher_text))
    #print(map[int(ph,16)])
    first_digit = map[int(pl,16)].index(int(cl,16))    
    second_digit = map[int(ph,16)].index(int(ch,16))
    print(first_digit,second_digit)
    return combine_digit(first_digit,second_digit)

print(chr(int(given_plaintext_ciphertext_find_key(0x20,0xee),16)))
#find key character given plain_text and cipher_text value