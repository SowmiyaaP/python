import random

letters =[ 'A', 'B', 'C', 'D', 'E', 'F', 'G','H', 'I', 'J', 'K', 'L', 
          'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' , 'a' , 'b' ,
        'c' ,'d' , 'e', 'f', 'g', 'h','i','j','k','l','m','n','o','p','q','r','s','t' ,'u' ,
        'v', 'w', 'x','y','z' ]
numbers = ['1' , '2' , '3', '4','5','6','7','8','9','0',]  
spl = ['!','"','#','$','%','&','()','*','+',',','-','.','/',':']
print("welcome to password generator \n")
let = int(input("how many letters: "))
sym = int(input("how many characters: "))
num = int(input("how many numbers: "))
pwd = ""

for ch in range(1,let+1):
    random_let = random.choice(letters)
    pwd += random_let

for sy in range(1,sym+1):
    random_sym = random.choice(spl)
    pwd += random_sym

for nu in range(1,num+1):
    random_num = random.choice(numbers)
    pwd += random_num

pwds = list(pwd)
random.shuffle(pwds)  

password=""
for n in pwds:
    password += n

print(f"Your password is {password}")