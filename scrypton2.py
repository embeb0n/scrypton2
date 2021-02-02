class console:
    def log(value, console):
        print(value)
    def ostream(value, console):
        print(value, end='')
    def istream(text, console):
        val = input(text)
        return val

class debug:
    def log(value):
        print(value)
    def ostream(value):
        print(value,end='')
    def istream(text):
        val = input(text)
        return val

class server:
    def log(value, server):
        print(value)
    def ostream(value, server):
        print(value, end='\n')

def serverOf(ip):
    return server

def int(val):
    return val
def string(val):
    return val
def rune(val):
    return val
def bool(val):
    return val
def float(val):
    return val
def double(val):
    return val

def listOf(type, size, value):
    list = []
    rage = range(0, size)
    for it in rage:
        list.append(value)
    return list