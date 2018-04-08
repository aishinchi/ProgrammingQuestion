import sys
if __name__ == "__main__":
    num = int(sys.stdin.readline().strip())
    strList = sys.stdin.readline().strip().split()
    array = []
    for i in range(num):
        array.append(int(strList[i]))
    minResult = abs(array[0] - array[1])
    maxResult = 0
    mincount = 0
    maxcount = 0
    for i in range(num-1):
        for j in range(i+1, num):
            temp = abs(array[i] - array[j])
            if minResult > temp:
                minResult = temp
                mincount = 1
            elif minResult == temp:
                mincount += 1
            elif maxResult < temp:
                maxResult = temp
                maxcount = 1
            elif maxResult == temp:
                maxcount += 1
    print(str(mincount) + " " + str(maxcount))