"""
갯수 T를 입력받아 입력받은 수 만큼 반복한다.
수를 입력받을 때 공백을 기준으로 연달아 2개를 입력받아 더한다.
"""

def sumForT(n):
    result = list()

    while (n != 0):
        sumOfResult = sum(map(int, input().split()))
        result.append(sumOfResult)

        n = n-1

    return result

if __name__ == '__main__':
    resultList = list()
    T = int(input())

    resultList = sumForT(T)

    for elem in resultList:
         print(elem)