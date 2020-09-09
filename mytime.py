import time


def insane_func():
    x = input('hi there, whatsyour name?')
    return x


def main():
    y = insane_func()
    print('hello', y)
    print('check out time mocule workd')
    time.sleep(5)


main()
