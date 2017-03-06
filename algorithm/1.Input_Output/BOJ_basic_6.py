if __name__ == '__main__':

    while (1):

        listInNumber = []
        listInNumber = list(map(int, input().split()))

        if (listInNumber[0] == 0) and (listInNumber[1] == 0):
            break

        print(sum(listInNumber))

