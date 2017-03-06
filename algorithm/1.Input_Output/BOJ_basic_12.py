"""
BOJ 11720 == 숫자의 합 == BOJ_basic_12

문제
N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주어진다.

출력
입력으로 주어진 숫자 N개의 합을 출력한다.
"""
if __name__ == '__main__':
    result = 0

    N = int(input())

    iInNumbers = list(map(int, input()))

    for number in range(N):
        result = result + iInNumbers[number]

    print(result)