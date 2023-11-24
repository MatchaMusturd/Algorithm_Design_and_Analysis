# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import random


class Optimalbt:
    def __init__(self):
        self.cc = []
        self.bpc = []
        self.wij = []
        self.np = []
        self.lp = []

    def grpoens(self, nn):
        # 在下面的代码行中使用断点来调试脚本。
        pl = []
        pl_ = []
        nal1 = 2 * nn
        for i in range(nal1):
            p = random.random()
            pl.append(round(p, 3))
        pl.sort()
        pl_.append(pl[0])

        for i in range(nal1)[:-1]:
            p1 = pl[i]
            p2 = pl[i + 1]
            mg1 = p2 - p1
            pl_.append(round(mg1, 3))
        tl = 1 - float(pl[-1])
        pl_.append(round(tl, 3))
        for i in range(len(pl_)):
            if i % 2 == 0:
                self.lp.append(pl_[i])
            else:
                self.np.append(pl_[i])

    def printwolists(self):
        np_ = [[], []]
        lp_ = [[], []]
        npl = len(self.np)
        lpl = len(self.lp)
        for i in range(npl):
            np_[0].append(i + 1)
            lp_[0].append(i + 1)
        lp_[0].append(lpl)
        np_[1] = self.np
        lp_[1] = self.lp
        blank = ' '
        print('list of nodes possiblility')
        for i in np_:
            for j in range(len(np_[0])):
                s = str(i[j])
                l1 = len(s) - 1
                l_ = 6 - l1
                print(f'{l_ * blank}{i[j]}', end='')
            print()
        print('list of leaves possiblility')
        for i in lp_:
            for j in range(len(lp_[0])):
                s = str(i[j])
                l1 = len(s) - 1
                l_ = 6 - l1
                print(f'{l_ * blank}{i[j]}', end='')
            print()

    def buildchart(self):
        l2 = len(self.np)

        for i in range(l2):
            self.cc.append([])
            self.bpc.append([])
            self.wij.append([])
            for j in range(l2):
                self.cc[i].append(0)
                self.bpc[i].append(0)
                self.wij[i].append(0)

        for i in range(l2):
            for j in range(l2 - i):
                # 每组循环的下界
                r = j + i  # 每组循环的上界
                minv = 0
                if i == 0:
                    self.cc[j][j] = round(self.np[j] + self.lp[j] + self.lp[j + 1], 3)
                    self.wij[j][j] = self.cc[j][j]
                    self.bpc[j][r] = j + 1
                else:
                    mi = 10
                    for w in range(j, r + 1):
                        # w代表在每个元素代表的e中的每个断点
                        # k = j + w
                        if w - 1 < j:
                            r_1 = 0
                        elif w - 1 == j:
                            r_1 = self.np[j]
                        else:
                            r_1 = self.cc[j][w - 1]

                        if w + 1 == r:
                            r_2 = self.np[r]
                        elif w + 1 > r:
                            r_2 = 0
                        else:
                            r_2 = self.cc[w + 1][r]

                        if r_1 + r_2 < mi:
                            mi = r_1 + r_2
                            self.bpc[j][r] = w + 1
                    self.wij[j][r] = round(self.wij[j][r - 1] + self.np[r] + self.lp[r + 1], 3)
                    minv += self.wij[j][r]
                    minv += mi
                    self.cc[j][r] = round(minv, 3)

    def printcharts(self):
        blank = ' '
        cc = self.cc
        bpc = self.bpc
        wij = self.wij
        l2 = len(self.np)
        cc.insert(0, [])
        bpc.insert(0, [])
        wij.insert(0, [])
        for i in range(l2):
            cc[0].append(i + 1)
            bpc[0].append(i + 1)
            wij[0].append(i + 1)

        count = 0
        for i in cc:
            i.insert(0, count)
            count += 1

        count = 0
        for i in bpc:
            i.insert(0, count)
            count += 1

        count = 0
        for i in wij:
            i.insert(0, count)
            count += 1

        print('the least cost')
        for i in cc:
            for j in range(l2 + 1):
                s = str(i[j])
                l1 = len(s) - 1
                l_ = 6 - l1
                print(f'{l_ * blank}{i[j]}', end='')
            print()
        print('break points')
        for i in bpc:
            for j in range(l2 + 1):
                s = str(i[j])
                l1 = len(s) - 1
                l_ = 6 - l1
                print(f'{l_ * blank}{i[j]}', end='')
            print()
        print('single aggregate cost')
        for i in wij:
            for j in range(l2 + 1):
                s = str(i[j])
                l1 = len(s) - 1
                l_ = 6 - l1
                print(f'{l_ * blank}{i[j]}', end='')
            print()

#
# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    num = int(input('\ninput the number of all nodes'))
    obt = Optimalbt()
    obt.grpoens(num)
    obt.printwolists()
    obt.buildchart()
    obt.printcharts()
# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
