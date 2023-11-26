def prime(num):
    for i in range(2, num):
        if num % i == 0:
            print("The number %d is not prime" % num)
            break
        else:
            print(("The number %d is prime" % num))
            break


n = int(input("Enter the Number:"))
prime(n)
