"""
접두사 배열
접미사 배열(suffix array)이란, 어떤 문자열의 모든 접미사를 사전 순으로 정렬한 뒤, 각 접미사의 시작 위치를 기록한 배열을 의미한다.
예를 들어 'banana' 라는 문자열에 대해 접미사 배열을 구한다면 아래와 같다

문자열의 모든 접미사는 아래와 같다.
banana, anana, nana, ana, na, a

위 접미사들을 사전 순으로 정렬하면 아래와 같다.
a, ana, anana, banana, na, nana

각 접미사의 원래 문자열에서의 시작 인덱스를 기록하면 아래와 같다.
5, 3, 1, 0, 4, 2
따라서 문자열 'banana'의 접미사 배열은 { 5, 3, 1, 0, 4, 2 } 가 된다.

그러면 문자열의 모든 접미사를 저장할 리스트 하나와 사전 순으로 변환했을 때 저장할 리스트 하나가 필요하다.
"""

inString = list(input())

suffixArray = list()
buffer = list()

for i in range(len(inString)):
    suffixArray.append(inString[i:])

buffer = suffixArray[:]
suffixArray.sort()

for index in range(len(buffer)):
    print(buffer.index(suffixArray[index]))

