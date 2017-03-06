"""
(A+B)%C는 (A%C + B%C)%C 와 같을까?

(A×B)%C는 (A%C × B%C)%C 와 같을까?

그냥 눈에 보이는 대로 풀면 될듯!
"""

if __name__ == '__main__':
    inNumber = list(input().split())
    result = list()

    A = int(inNumber[0])
    B = int(inNumber[1])
    C = int(inNumber[2])

    result.append((A+B)%C)
    result.append((A%C + B%C)%C)
    result.append((A*B)%C)
    result.append(((A%C)*(B%C))%C)

    for x in range(len(result)):
        print(result[x])