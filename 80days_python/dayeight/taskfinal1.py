from quopri import decodestring


alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
        'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' , 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
        'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
#text and plain is the arguement and message and shift_val is parameter
def encrypt (t,s):
    cipher_text = ""
    for i in alpha:
        pos = alpha.index(i)
        new_pos = pos + s
        new_i = alpha[new_pos]
        cipher_text += new_i
    print(f"The encrypted code is {cipher_text}")  

encrypt(text,shift)    

def decrypt (t,s):
    t = ""
    for i in alpha:
        pos = alpha.index(i)
        new_pos = pos - s
        new_i = alpha[new_pos]
        t += new_i
    print(f"The encrypted code is {t}")

if direction == "encode":
    encrypt(text,shift) 
else:
    decrypt(text,shift)


