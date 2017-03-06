"""
2진수를 8진수로 변환하는 프로그램

round() : 반올림하는 함수.
round(x +0.5) : 올림하는 함수.

입력받은 리스트의 수를 맨뒤에서 부터 계산해야함.


if __name__ == '__main__':
    listOfRange = [1, 2, 4]
    resultOfList = list()
    inBinary = [int(number) for number in input()]
    inBinary.reverse()

    for i in range(round((len(inBinary)/3)+0.5)):
        result = 0

        for j in range(3):
            if (j + 3*i) < len(inBinary):
                result = result + (inBinary[j + 3 * i] * listOfRange[j])

            else:
                break

        resultOfList.append(result)

    resultOfList.reverse()

    for i in range(len(resultOfList)):
        print(resultOfList[i])

        시도했던 소스
"""

# 이거 어디서 가져온 소스
N = int(input(), 2)
N = oct(N)

print(N[2:])