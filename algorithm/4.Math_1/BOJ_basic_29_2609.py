"""
두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.
최소 공약수 예제는 위키피디아
https://ko.wikipedia.org/wiki/%EC%9C%A0%ED%81%B4%EB%A6%AC%EB%93%9C_%ED%98%B8%EC%A0%9C%EB%B2%95

유클리드 호제법 = 최대 공약수를 구하는 알고리즘
https://opentutorials.org/course/1685/9533

최소공배수는 최대공약수와는 반대로, 두 정수가 공통적으로 가지는 배수 중 가장 작은 값을 의미합니다.
최소공배수는 최대공약수와 밀접한 관계가 있는데, 정수 a, b의 최대공약수 G = gcd(a, b)에 대하여 아래의 식을 만족하는 정수 x와 y가 존재합니다.

 a = Gx, b = Gy (단, x, y는 정수)

 이 때 a * b = G*G*x*y 임을 알 수 있고, G는 두 수의 최대 공약수이며 x와 y는 서로소인 관계를 가집니다. 집합적으로 생각하면,
 a와 b의 합집합은 G, x, y이고 이 세 수를 곱한 G*x*y가 최소공배수가 됨을 알 수 있습니다.
 그러므로 두 수의 최소공배수 L = lcm(a, b)은 L= lcm(a, b)= a * b / gcd(a, b)이 성립합니다.
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
    inNumber = list(input().split())

    a = int(inNumber[0])
    b = int(inNumber[1])

    gcd = gcd(a,b)
    lcm = lcm(a,b, gcd)

    print(gcd)
    print(lcm)
