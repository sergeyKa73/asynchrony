from time import sleep

deque = []


def counter():
    counter = 0
    while True:
        print(counter)
        counter += 1
        yield


def printer():
    counter = 0
    while True:
        if counter % 3 == 0:
            print('Bang!')
        counter += 1
        yield


def main():
    while True:
        g = deque.pop(0)
        next(g)
        deque.append(g)
        sleep(0.5)


if __name__ == '__main__':
    g1 = counter()
    deque.append(g1)
    g2 = printer()
    deque.append(g2)
    main()
