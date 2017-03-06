"""
python에서 나눗셈은 x/y는 소수점까지 나타낸다.
ex ) 13/2 = 6.5 그래서 int형으로 변환해주고 몫과 나머지를 구해야한다.

재귀의 특성을 꼭 알도록하자.
재귀로 풀면 list.reverse() 가 필요없다.

http://browoo.tistory.com/entry/%EB%AC%B8%EC%A0%9C11005-%EC%A7%84%EB%B2%88-%EB%B3%80%ED%99%98-2
위 링크의 예제 소스를 많이 참고하였고, 재귀함수의 특성을 알 수 있었다.

"""

def base(N, B):


    if (N != 0):
        base(N//B, B)
        #print(N, B) ;; 재귀 함수의 특징을 알 수 있다.
        if (N%B)>9:
            print(chr(ord('A') + (N%B - 10)))
        else:

            print(N%B)


if __name__ == '__main__':
    inNumber = [int(x) for x in input().split()]

    N = inNumber[0]
    B = inNumber[1]

    base(N, B)

