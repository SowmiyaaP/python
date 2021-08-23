def prime(num):
    if num >1:
        for i in range(2,num):
            if (num % i == 0):
                print("It's not a prime number")
                break
            else:
                print("It's  a prime number")    
    else:
        print("It is not a prime number")
n = int(input("Enter the number: "))
prime(n)        