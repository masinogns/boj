"""
gcd의 합
for (int i = 0; i < n; i++) {
    num[i] = gcd( num[i], num[i-1] )
 }
 구현.

 https://github.com/Yukariko/acm/blob/master/problem/9613/test.c

 https://wikidocs.net/3086
 for와 range를 통해 이중for문 구현

 예를 들어, 4 10 20 30 40 일 때
 gcd(10, 20)    gcd(20, 30)     gcd(30, 40)
 gcd(10, 30)    gcd(20, 40)
 gcd(10, 40)

 이렇게 다 더한 값을 원한다.
"""

def gcd(a, b):
    mod = a%b

    while (mod > 0):
        a = b
        b = mod
        mod = a%b

    return b

if __name__ == '__main__':
    result = list()

    T = int(input())

    for x in range(T):
        inNumber = [int(number) for number in input().split()]
        gcdSum = 0

        for number in range(1, inNumber[0]):
            for i in range(number+1, inNumber[0]+1):
                gcdSum = gcdSum + gcd(inNumber[number], inNumber[i])


        print(gcdSum)

