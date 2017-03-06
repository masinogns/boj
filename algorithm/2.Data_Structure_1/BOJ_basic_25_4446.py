"""
위치 이동 논리

vowel[ index + 3 % 6 ]
consonant [ index + 10 % 20 ] 를 이용해서 위치 이동을 사용한다.
"""

if __name__ == '__main__':
    # vowel은 6개의 문자들, consonant는 20개의 문자들
    vowel = ['a', 'i', 'y', 'e', 'o', 'u']
    consonant = ['b', 'k', 'x', 'z', 'n', 'h', 'd', 'c', 'w', 'g', 'p', 'v', 'j', 'q', 't', 's', 'r', 'l', 'm', 'f']
    result = list()
    inString = list(input())



    for i in range(len(inString)):
        for index in range(len(vowel)) :
            if inString[i] == vowel[index]:
                vowelValue = (index + 3) % 6
                result[i] = vowel[vowelValue]




    print(result)