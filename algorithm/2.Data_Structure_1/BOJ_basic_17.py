"""
BOJ_basic_14 : 스택 문제 참고
"""
if __name__ == '__main__':
    queue = list()

    N = int(input())

    for numbers in range(N):
        InputCommand = list(input().split())
        queueSize = len(queue)

        if InputCommand[0] == "push":
            queue.append(InputCommand[1])

        elif InputCommand[0] == "pop":
            if queueSize != 0:
                print(queue[0])
                del queue[0]
            else:
                print(-1)

        elif InputCommand[0] == "size":
            print(queueSize)

        elif InputCommand[0] == "empty":
            if queueSize != 0:
                print(0)
            else:
                print(1)

        elif InputCommand[0] == "front":
            if queueSize != 0:
                print(queue[0])
            else:
                print(-1)

        elif InputCommand[0] == "back":
            if queueSize != 0:
                print(queue[queueSize-1])
            else:
                print(-1)