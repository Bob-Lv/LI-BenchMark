import sys
import os
import time
print("欢迎使用性能测试工具")
print("正在测试：1百万次列表信息插入")
start_time=time.time()
list1=[]
c=0
for a in range(0,1000):
    for b in range(0,1000):
        list1.insert(0,0)
        c+=1
        percentage = round(c / 1000000 * 100)
        print("\r进度: {}%: ".format(percentage), "▓" * (percentage // 2), end="")
        sys.stdout.flush()
end_time=time.time()
print("")
print("用时:",end_time-start_time,"秒","(越短越好)")
os.system("pause")