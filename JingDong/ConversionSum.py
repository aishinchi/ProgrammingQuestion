import sys


def Convert(original, tempNum, count):
    a, b = divmod(original, tempNum)
    count += b
    if a:
        return Convert(a, tempNum, count)
    else:
        return count

def Reduction(count, num):
    ret = 1
    while count % num:
        tmp = count % num
        count = num
        num = tmp
    ret = num
    return ret

if __name__ == "__main__":
    number = []
    for line in sys.stdin:
        strNum = line.strip()
        number.append(int(strNum))
    lens = len(number)
    for i in range(lens):
        if number[i] == 1:
            print(str(1) + "/" + str(1))
        elif number[i] == 2:
            print(str(2) + "/" + str(1))
        else:
            count = 0
            num = number[i] - 2
            for j in range(num):
                tempCount = Convert(number[i], 2 + j, 0)
                count += tempCount
            con = Reduction(count, num)
            count = int(count / con)
            num = int(num / con)
            print(str(count) + "/" + str(num))

