# 例1. 简单输出斐波那契數列前 N 个数
# 缺点：该函数可复用性较差，因为 fab 函数返回 None，其他函数无法获得该函数生成的数列
# 要提高 fab 函数的可复用性，最好不要直接打印出数列，而是返回一个 List。
def fab1(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b, end=' ')
        a, b = b, a + b
        n = n + 1


fab1(5)
print('\n')


# 例 2.
# 缺点：该函数在运行中占用的内存会随着参数 max 的增大而增大，如果要控制内存占用，
# 最好不要用 List 来保存中间结果，而是通过 iterable 对象来迭代
def fab2(max):
    n, a, b = 0, 0, 1
    L = []
    while n < max:
        L.append(b)
        a, b = b, a + b
        n = n + 1
    return L


# 例3
# 说明：带有 yield 的函数不再是一个普通函数，Python 解释器会将其视为一个 generator，
# 调用 fab(5) 不会执行 fab 函数，而是返回一个 iterable 对象！
# 在 for 循环执行时，每次循环都会执行 fab 函数内部的代码，执行到 yield b 时，fab 函数就返回一个迭代值，
# 下次迭代时，代码从 yield b 的下一条语句继续执行，而函数的本地变量看起来和上次中断执行前是完全一样的，
# 于是函数继续执行，直到再次遇到 yield。
def fab3(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1


f = fab3(5)
print("f是一个可迭代对象，并没有执行函数")
print(f)
print('fab3返回的是一个iterable 对象，可以用for循环获取值')
for n in f:
    print(n)
    print("========")


# 例4：
# 说明：yield from iterable本质上等于for item in iterable: yield item的缩写版

def f_wrapper1(f):
    for g in f:
        yield g


wrap = f_wrapper1(fab3(5))
for i in wrap:
    print(i, end=' ')


def f_wrapper2(f):
    print('\n使用yield from代替for循环')
    yield from f  # 注意此处必须是一个可生成对象


wrap = f_wrapper2(fab3(5))
for i in wrap:
    print(i, end=' ')
print('\n---------------------')


def g(x):
    print('yield from包含多个子程序。 A迭代完，再开始迭代B')
    yield from range(x, 0, -1)  # A
    yield from range(x)  # B


print(list(g(5)))
for g in g(6):
    print(g, end=',')

print('\n---------------------')
# 注意红色部分就是替代的部分，yield from iterable本质上等于for item in iterable: yield item的缩写版
