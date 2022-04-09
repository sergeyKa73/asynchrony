import time


def gen(s):
    for i in s:
        yield i


def gen_filename():
    while True:
        pattern = 'file-{}.jpeg'
        t = int(time.time() * 1000)

        print('Name create')
        yield pattern.format(str(t))

        print(time.strftime("%H:%M:%S", time.gmtime()))


# g = gen_filename()
#
# while True:
#     print(next(g))
#     time.sleep(1)

def gen1(s):
    for i in s:
        yield i

def gen2(n):
    for i in range(1, n+1):
        yield i

g1 = gen1('sergey')
g2 = gen2(6)

tasks = [g1, g2]

while tasks:
    task = tasks.pop(0)

    try:
        i = next(task)
        print(i)
        tasks.append(task)
    except StopIteration:
        pass

