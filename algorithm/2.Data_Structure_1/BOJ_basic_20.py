"""
https://pymotw.com/2/collections/deque.html
deque 참고 자료.
"""

from collections import deque

if __name__ == '__main__':

    d = deque()

    N = int(input())

    for number in range(N):
        inCommand = input().split()

        if inCommand[0] == "push_front":
            d.appendleft(inCommand[1])

        elif inCommand[0] == "push_back":
            d.append(inCommand[1])

        elif inCommand[0] == "pop_front":
            if len(d) != 0:
                print(d.popleft())
            else:
                print(-1)

        elif inCommand[0] == "pop_back":
            if len(d) != 0:
                print(d.pop())
            else:
                print(-1)

        elif inCommand[0] == "size":
            print(len(d))

        elif inCommand[0] == "empty":
            if len(d) != 0:
                print(0)
            else:
                print(1)

        elif inCommand[0] == "front":
            if len(d) != 0:
                print(d[0])
            else:
                print(-1)

        elif inCommand[0] == "back":
            if len(d) != 0:
                print(d[len(d)-1])
            else:
                print(-1)


