# scope 

# global scope
x = 10

def foo():
    # local scope
    x = 20
    print(x)

foo()
print(x)

def func():
    num = 10
    print(locals())

func()

print(globals())

