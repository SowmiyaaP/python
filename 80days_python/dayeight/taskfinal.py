alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
#text and plain is the arguement and message and shift_val is parameter
def encrypt(message,shift_val):
    chiper_text = ""
    for i in alphabet:
       pos = alphabet.index(i)
       new_pos = pos + shift_val
       new_let = alphabet[new_pos]
       chiper_text += new_let
    print(f"The encoded text is {chiper_text}")
            
encrypt(message=text,shift_val=shift)


