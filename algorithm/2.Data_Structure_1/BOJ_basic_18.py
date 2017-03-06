"""
조세퍼스 문제

원형 탁자에 N명이 있고 M(<= N)은 M번째 사람을 제거하라는 의미이다.
N명이 모두 제거될 때까지 계속된다. -> while or for문으로 구현한다.
원에서 사람들이 제거되는 순서는 다음과 같다.
(N, M)으로 del로 구현할 수 있고 의미는 N 명중에서 M번째 사람을 계속해서 제거해 나가라.

원형 큐로 풀어야 하는 문제인것 같다.
그럼 큐가 0, 1, 2, 3, 4, 5, 6 으로 이루어 져 있을 때 0에서 6으로 그리고 6에서 0으로 가는 논리만 구현하면 원형 큐로 쉽게
풀 수 있을 것 같다.

큐는 클래스로 한 번 구현해 보도록 한다.
https://www.acmicpc.net/board/view/8723
소스 참고하다.

원형 큐 만드는 방법

    front = Q.front()
    print(front)

    Q.get()
    print(Q.queue)

    Q.put(front)
    print(Q.queue)

[3, 5, 6] ---> <3, 5, 6> 이렇게 변환시키는 방법은?

https://godoftyping.wordpress.com/2015/04/24/python-%EB%8D%B0%ED%81%ACdeque/
python deque 참고자료.

http://sarangyik.tistory.com/entry/Pythonmodule-queue
python moduel queue 참고자료.

https://docs.python.org/3.1/tutorial/datastructures.html
리스트로 스택, 큐 만드는 방법
"""

class Queue:
    def __init__(self):
        self.queue = list()

    def put(self, pushParams):
        self.queue.append(pushParams)

    def get(self):
        if len(self.queue) != 0:
            self.queue.pop(0)
        else:
            print("Do not get func")

    def front(self):
        result = 0

        if len(self.queue) != 0:
            result = self.queue[0]
        else:
            result = -10

        return result

    def back(self):
        result = 0

        if len(self.queue) != 0:
            result = self.queue[len(self.queue) - 1]
        else:
            result = -20

        return result

if __name__ == '__main__':
    Q = Queue()
    resultList = list()
    counter = 0

    InNumber = list(input().split())
    N = int(InNumber[0])
    M = int(InNumber[1])

    for numbers in range(N):
        Q.put(numbers + 1)

    print("<")
    while (len(Q.queue) != 0):
        front = Q.front()
        Q.get()
        counter = counter+ 1

        if counter == M:
            print(front)
            counter = 0
            if len(Q.queue) != 0:
                print(", ")

        else:
            Q.put(front)

    print(">")
