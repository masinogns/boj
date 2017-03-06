"""
http://mwultong.blogspot.com/2007/01/python-ascii-code-char.html
파이썬 문자를 아스키 코드로, 아스키 코드를 문자로

http://egloos.zum.com/mcchae/v/11009428
리스트 초기값으로 설정
"""
if __name__ == '__main__':
    result = list()
    inWord = list(input())

    for j in range(26):
        result.append(0)

    for i in range(len(inWord)):
        char = inWord[i]
        asciiCode = ord(char)
        index = asciiCode-97

        result[index] = result[index] + 1

    for x in range(26):
        print(result[x])