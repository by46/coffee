import os


def worker():
    print os.getcwd()
    pid = os.fork()
    if pid == 0:
        print 'children'
        return
    print 'parent', pid

if __name__ == '__main__':
    worker()
