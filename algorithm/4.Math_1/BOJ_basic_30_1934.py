"""
BOJ_basic_29_2609의 최대공약수와 최소공배수 소스를 가져와서 활용.
"""

def gcd(a, b):
    mod = a%b

    while (mod > 0):
        a = b
        b = mod
        mod = a%b

    return b

def lcm(a, b, gcd):
    return int((a*b)/gcd)

if __name__ == '__main__':

    TestNumber = int(input())

    for number in range(TestNumber):

        inNumber = [int(number) for number in input().split()]

        a = inNumber[0]
        b = inNumber[1]

        gcdNumber = gcd(a,b)
        lcmNumber = lcm(a,b, gcdNumber)

        print(lcmNumber)

