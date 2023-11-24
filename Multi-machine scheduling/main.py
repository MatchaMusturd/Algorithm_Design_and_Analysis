# 这是一个示例 Python 脚本。
import numpy as np
# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
class Multimachinediapatch():
    def __init__(self, number):
        self.jobslength = []
        self.multilist = []
        self.sum_ = []
        self.sm = 0

        for i in range(number):
            self.multilist.append([])
            self.sum_.append(0)
        self.le = len(self.multilist)

    def inputjob(self):
    # 在下面的代码行中使用断点来调试脚本。
        count = 0
        print('input all jobs lengh(print . to exit)')
        while True:
            count += 1
            ip = input(f'{count}  ')
            if ip == '.':
                break
            else:
                self.jobslength.append(int(ip))

        self.jobslength.sort()
        self.sm = sum(self.jobslength)
        print(self.jobslength)

    def dealwith(self):
        l = len(self.jobslength)
        l_ = len(self.multilist)

        while l != 0:
            count = 0
            # first = self.jobslength[0]
            big =  self.jobslength.pop()
            l = len(self.jobslength)
            for i in self.multilist:
                if len(i) == 0:
                    i.append(big)
                    break
                else:
                    count += 1
            if count == l_:
                s = 1000
                for i in range(l_):
                    list_ = self.multilist[i]
                    self.sum_[i] = sum(list_)
                    if sum(list_) < s:
                        s = sum(list_)
                index_ = self.sum_.index(s)
                self.multilist[index_].append(big)
                self.sum_[index_] = sum(self.multilist[index_])
        # for i in self.sum_:
        #     print(i)

    def printresult(self):
        bk = ' '
        count = 0
        for i in self.multilist:
            count += 1
            print(f'number {count} machine')
            for j in i:
                s = str(j)
                l1 = len(s)
                l2 = 5 - l1
                print(f'{l2 * bk}{j}', end='')
            sm = sum(i)
            print(f'\nall jobs done need {sm}')
        allworkdone = max(self.sum_)
        average = np.mean(self.sum_)

        # print(self.sm, le)
        # av = self.sm / self.le
        print(f'finish all jobs need {allworkdone}')
        print(f'all machines average finish time is {round(average, 3)}')
        # print(f'all machines average finish time(expected value) is {round(av, 3)}')

# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    noparallel = int(input('\ninput number of parallel machines'))
    m = Multimachinediapatch(noparallel)
    m.inputjob()
    m.dealwith()
    m.printresult()
# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
