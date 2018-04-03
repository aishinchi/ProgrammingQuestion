# -*- coding:utf-8 -*-
#这个真的巨坑，输入不止一组字符串，从下面的示例根本看不出来。。。冷漠
import sys
if __name__ == "__main__":
    stringList = []
    for line in sys.stdin:
        temp = line.split()
        stringList.extend(temp)
    lens = len(stringList)
    for j in range(lens):
        caps = ""
        lower = ""
        string = stringList[j]
        for i in range(len(string)):
            if string[i] >= "A" and string[i] <= "Z":
                caps += string[i]
            else:
                lower += string[i]
        print(lower+caps)