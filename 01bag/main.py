# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
class P:
    def __init__(self, c):
        self.chart = []
        self.item = []
        self.vl = []
        self.wl = []
        self.cap = c
    def ivaw(self):
        count = 0
        print('\ninput weight and value of each item(input . to exit)')
        while True:
            w = input('weight:')
            if w == '.':
                break
            v = input('value:')
            count += 1
            self.wl.append(int(w))
            self.vl.append(int(v))
        l = len(self.wl)
        for i in range(l):
            print(f'{i}   {self.wl[i]}:{self.vl[i]}')
        for i in range(l):
            self.chart.append([])
        for i in self.chart:
            for j in range(self.cap):
                i.append(0)

    def oper(self):
        l = len(self.wl)
        for i in range(l):
            for j in range(self.cap):
                if j + 1 < self.wl[i]:

                    self.chart[i][j] = self.chart[i - 1][j]
                else:
                    value = self.vl[i]
                    weight = self.wl[i]
                    dtp = self.chart[i - 1][j]
                    if i - 1 < 0:
                        dtp = 0
                        pt = value
                    elif  j  + 1 - weight <= 0:
                        pt = value
                    else:
                        pt = self.chart[i - 1][j - weight] + value
                    if pt > dtp:
                        self.chart[i][j] = pt
                    else:
                        self.chart[i][j] = dtp
        self.chart.insert(0,[])
        for i in range(self.cap):
            self.chart[0].append(i + 1)
        count = 0
        for i in self.chart:
            i.insert(0, count)
            count += 1
            for j in i:
                if j > 9:
                    print(f'{j}', end=' ')
                else:
                    print(f'{j}',end='  ')
            print()

    def traceback(self):
        l = len(self.wl)
        cv = self.chart[l][self.cap]
        # print(f'cv={cv}')
        index = self.cap
        for i in range(l - 1, 0, -1):
            if cv != self.chart[i][index]:
                v_ = cv - self.vl[i]
                # print(f'v_ {v_}')
                for j in range(index, 0, -1):
                    if self.chart[i][j] == v_:
                        cv = v_
                        self.item.insert(0, i + 1)
                        index = j
                        # print(j)
                        break
        self.item.insert(0, 1)
        print(f'the number of items are {self.item}')

# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    cap = int(input('\ninput capacity of the bag'))
    pa = P(cap)
    pa.ivaw()
    pa.oper()
    pa.traceback()
# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
