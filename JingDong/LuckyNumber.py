import sys


def Convert(original, tmpNum, count):
    a, b = divmod(original, tmpNum)
    count += b
    if a:
        return Convert(a, tmpNum, count)
    else:
        return count


if __name__ == "__main__":
    number = []
    for line in sys.stdin:
        tempStr = line.strip()
        number.append(int(tempStr))
    lens = len(number)
    for i in range(lens):
        numCount = 0
        for j in range(number[i]+1):
            binarySum = Convert(j, 2, 0)
            decimalSum = Convert(j, 10, 0)
            if binarySum == decimalSum:
                print(j)
                numCount += 1
        #不包括0
        print(numCount-1)