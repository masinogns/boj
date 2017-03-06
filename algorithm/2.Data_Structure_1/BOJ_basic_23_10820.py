"""
내가 생각한 문제 풀이 방법
https://namu.wiki/w/%EC%95%84%EC%8A%A4%ED%82%A4%20%EC%BD%94%EB%93%9C
아스키 코드를 이용하여 푼다.

숫자 48 ~ 57, 대문자 65 ~ 90, 소문자 97 ~ 122, 공백 space 32

테스트 케이스가 주어지지 않은 것은
while(1):
    if ~~~~~ == "":
        break
를 이용하여 해결하면 된다.

https://www.acmicpc.net/board/view/8527
질문 검색에서 찾음.
다시 봐야할 필요가 있음.
특히 print의 경우
print(a, b, c, d, sep=" ") 이렇게했는데
4 0 0 0 출력이 이렇게 나온다.
"""

if __name__ == '__main__':
    while True:
        st = input()
        if st == "":
            break
        a, b, c, d = 0, 0, 0, 0
        for x in st:
            if 'a' <= x and x <= 'z':
                a = a + 1
            elif 'A' <= x and x <= 'Z':
                b = b + 1
            elif '0' <= x and x <= '9':
                c = c + 1
            else:
                d = d + 1

        print(a, b, c, d, sep=" ")