def isPrime(num):

    isBool = True

    if (num<=1):
        isBool = False

    for i in range(2, num+1):
        if (num % i) == 0:
            isBool = False

    return isBool

if __name__ == '__main__':
    count = 0
    N = int(input())

    for i in range(N):
        number = int(input())

        if (isPrime(number)):
            count = count + 1

    print(count)