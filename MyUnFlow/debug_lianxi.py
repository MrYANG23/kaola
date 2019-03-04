#-*-coding:utf-8-*-
def foo(bar=[]):
    bar.append('bar')
    return bar
print(foo())
print(foo())