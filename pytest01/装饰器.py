'''
装饰器：运行中增加功能的一种法式
'''

'''
已经写好了一些测试用例，后面维护代码时，想增强这些用例的功能，比如增加日志。又不想改test_case1、test_case2的代码。
将写日志的功能定义成一个装饰器。装饰器是拿函数作为参数。
'''

def log(func):
    # *args,**kw的目：func可以有任意个参数
    def wrapper(*args,**kw):
        print(f"in 函数{func.__name__}")    #__name__每个函数都有，返回函数名
        func(*args,**kw)
        print(f"out 函数 :{func.__name__}")

    return  wrapper

def test_case1():
    print("in 函数:test_case1")
    print("测试用例1")
    print("out 函数:test_case2")

@log
def test_case2():
    print("测试用例2")

@log
def test_case3():
    print("测试用例3")