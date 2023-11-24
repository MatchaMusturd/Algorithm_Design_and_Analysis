# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import numpy

def print_hi(num):
    # 在下面的代码行中使用断点来调试脚本。
    fibo = []
    a = 1
    b = a * 2
    fibo.append(a)
    fibo.append(b)
    for i in range(num)[2:]:
        c = a + b
        fibo.append(c)
        a = b
        b = c
    # print(fibo)
    return fibo

def Huffman(f):
    f_ = f.copy()
    hl = []
    c = 0

    for i in range(len(f)):
        hl.append([])
    # interim = []
    while len(f_) > 1:
        a = f_[0]
        b = f_[1]
        l = len(f) - len(f_)
        # print(l)
        # print(f_)
        if a == c:
            for i in range(l + 1):
                hl[i].insert(0, 0)
            hl[l + 1].insert(0, 1)
        elif b == c:
            for i in range(l + 1):
                hl[i].insert(0, 1)
            hl[l + 1].insert(0, 0)
        else:
            hl[l + 1].insert(0, 1)
            hl[l].insert(0, 0)

        c = a + b
        # print(c)
        for i in range(len(f_)):

            if c > f_[i]:
                if i == len(f_) - 1:
                    f_.append(c)
                else:
                    continue
            else:
                f_.insert(i, c)
                break
        f_.pop(0)
        f_.pop(0)
        # print(f_)
    return hl


# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    number = int(input('\ninput number of Fibonacci list'))
    if number > 1:
        fibonacci = print_hi(number)
        print(f'{fibonacci}\n')
        h = Huffman(fibonacci)
        for i in h:
            print(i)
    else:
        print('please input a number bigger than 1\n')

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
