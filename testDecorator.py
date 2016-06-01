import time
from functools import reduce
from time import ctime, sleep

def now():
    # print time.localtime()
    print (time.time())

def log(func):
    def wrapper(*args, **kw):
        print ('call %s():' %func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print ('2013-12-25')
    # print (1)
now()


def tsfunc(func):
    def wrappedFunc():
        print '[%s] %s() called' % (ctime(), func.__name__)
        return func()
    return wrappedFunc

@tsfunc
def foo():
    pass

foo()
sleep(4)

for i in range(2):
    sleep(1)
    foo()

