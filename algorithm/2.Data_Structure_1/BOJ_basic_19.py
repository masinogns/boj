"""
BOJ_basic_19 : 에디터 : BOJ 1406
https://www.acmicpc.net/board/view/11623
참고 자료.

스택을 2개로 구현하여 커서를 기준으로 왼쪽은 왼쪽 스택, 오른쪽은 오른쪽 스택으로 칭하여 푼다.
커서의 이동 시, 삭제 시 그리고 추가 시 행위는 각 스택의 pop과 push로 이루어진다.
이 때, 각 pop된 요소들은 push 요소로 들어갈 수도 있음을 명심하자.

print("".join(stackL.stack) + "".join(stackR.stack))
http://mwultong.blogspot.com/2006/12/python-join-list-array.html
참고
"""
class Stack:
    def __init__(self):
        self.stack = list()

    def push(self, params):
        self.stack.append(params)

    def pop(self):
        if len(self.stack) > 0 :
            del self.stack[len(self.stack) - 1]
        else:
            print("Do not continue pop")

    def front(self):
        result = 0

        if len(self.stack) != 0:
            result = self.stack[len(self.stack) - 1]
        else:
            result = -10

        return result

if __name__ == '__main__':
    stackL = Stack()
    stackR = Stack()

    inString = list(input())
    N = int(input())

    stackL.stack = inString[:]

    for number in range(N):
        inCommand = input().split()
        command = inCommand[0]
        if len(inCommand) == 2:
            params = inCommand[1]

        if command == "L":
            if len(stackL.stack) != 0:
                front = stackL.front()
                stackL.pop()
                stackR.push(front)
            else:
                continue

        elif command == "D":
            if len(stackR.stack) != 0:
                front = stackL.front()
                stackR.pop()
                stackL.push(front)
            else:
                continue

        elif command == "B":
            if len(stackL.stack) != 0:
                stackL.pop()
            else:
                continue
        elif command == "P":
            stackL.push(params)

    #print(stackL.stack + stackR.stack)
    print("".join(stackL.stack) + "".join(stackR.stack))

