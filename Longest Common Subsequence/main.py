# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
class Struc:
    def __init__(self, lista, listb, list):
        # self.multic = {}
        self.abcommen = []
        self.list = list
        self.lista = lista
        self.listb = listb
        self.c = 0
    def ftbcs(self):
        la = len(self.lista)
        lb = len(self.listb)
        for i in range(la):
            for j in range(lb):
                if self.lista[i] == self.listb[j]:
                    # print(self.lista[i])
                    if i - 1 < 0 or j - 1 < 0:
                        self.list[i][j] = 1
                    else:
                        self.list[i][j] = self.list[i - 1][j - 1] + 1
                else:
                    if i - 1 < 0:
                        self.list[i][j] = self.list[i][j - 1]
                    elif j - 1 < 0:
                        self.list[i][j] = self.list[i - 1][j]
                    else:
                        if self.list[i - 1][j] < self.list[i][j - 1]:
                            self.list[i][j] = self.list[i][j - 1]
                        else:
                            self.list[i][j] = self.list[i - 1][j]
        print()

    def gc(self):
        a = len(lista_)
        b = len(listb_)
        # ac = []
        while a != 0 and b != 0:

            ab = self.list[a - 1][b - 1]
            if a <= 1:
                ab_ = self.list[a - 1][b - 2]
                a_b_ = 0
                a_b = 0
            elif b <= 1:
                a_b = self.list[a - 2][b - 1]
                ab_ = 0
                a_b_ = 0
            else:
                a_b_ = self.list[a - 2][b - 2]
                a_b = self.list[a - 2][b - 1]
                ab_ = self.list[a - 1][b - 2]


            if a_b == ab > ab_ == a_b_:
                a -= 1
                # self.abcommen.insert(0, self.lista[a - 1])
            elif ab_ == ab > a_b == a_b_:
                b -= 1
                # self.abcommen.insert(0, self.listb[b - 1])
            elif a_b == a_b_ == ab_ == ab:
                a -= 1
                b -= 1
            elif a_b == a_b_ == ab_ < ab:
                self.abcommen.insert(0, self.listb[b - 1])
                a -= 1
                b -= 1
            elif ab_ == a_b == a_b > a_b_:
                a -= 1
                # self.abcommen.insert(0, self.lista[a - 1])
        print(f'\n{self.abcommen}')


# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    lista_ = input('\nfirst string:')
    listb_ = input('second string:')
    la = len(lista_)
    lb = len(listb_)
    l = []
    for i in range(la):
        l.append([])
    for i in l:
        for j in range(lb):
            i.append(0)
    sc = Struc(lista_, listb_, l)
    sc.ftbcs()
    for i in sc.list:
        print(i)
    sc.gc()
# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
