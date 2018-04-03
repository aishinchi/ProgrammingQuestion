import sys
if __name__ == "__main__":
    num = int(sys.stdin.readline().strip())
    strList = sys.stdin.readline().strip().split()
    array = []
    for i in range(num):
        array.append(int(strList[i]))
    result = dict()
    for i in range(num-1):
        for j in range(i+1, num):
            temp = abs(array[i] - array[j])
            if temp in result:
                result[temp] += 1
            else:
                result[temp] = 1
    minResult = min(result.keys())
    maxResult = max(result.keys())
    print(str(result[minResult]) + " " + str(result[maxResult]))