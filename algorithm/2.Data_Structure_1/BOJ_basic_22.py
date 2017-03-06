"""
먼저 알파벳 소문자로만 이루어진 문자열을 입력받는다.
입력받은 문자열을 분석할 것인데

b a e 를 입력받으면, b가 1번째 a가 2번째 e가 3번째 이므로

a의 위치, b의 위치, e의 위치를
    1       0           2

결과 배열 즉, a를 찾았으면 'a'를 ord() 함수를 이용해서 ascii 코드로 변환한 후
'a' = 97을 이용하여 index = x - 97을 수식연산하여 index의 값을 알아낸다.
그럼 해당 알파벳의 위치에 갈 수 있다.
for 문을 이용하여 0번째부터 알파벳의 위치를 찾아 갈 수 잇다.
"""

if __name__ == '__main__':
    result = list()
    inWord = list(input())

    for j in range(26):
        result.append(-1)

    for i in range(len(inWord)):
        char = inWord[i]
        asciiCode = ord(char)
        index = asciiCode - 97

        if result[index] == -1 :
            result[index] = i
        else:
            continue

    for x in range(len(result)):
        print(result[x])