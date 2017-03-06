"""
쉬움

문자열로 받아들여 두 문자열씩 붙이고
붙인 문자열을 int형으로 바꿔주어 연산을 하면 된다.

"""
inString = list(input().split())

result = list()
result.append(inString[0] + inString[1])
result.append(inString[2] + inString[3])

resultNumber = int(result[0]) + int(result[1])
print(resultNumber)