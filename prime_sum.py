def findPrime(number):
    for i in range(2, number):
        if (number % i == 0):
            return 0
    return number

def sumOfPrime(n):
    Sum = 0
    for i in range(2, n+1):
        Sum = Sum + findPrime(i)
    return Sum

print(sumOfPrime(5))