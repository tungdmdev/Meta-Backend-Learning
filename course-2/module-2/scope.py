#global scope
my_global = 10

def fn1():
    enclosed_v = 8

    def fn2():
        local_v = 5
        print('Access to global', my_global)
        print('Access to enclosed', enclosed_v)
    fn2()

fn1()

#local
def get_total(a, b):
    #local variable declared inside a function
    total = a + b
    return total

print(get_total(5, 2))

#Enclosing scope
def get_total(a, b):
    #enclosed variable declared inside a function
    total = a + b

    def double_it():
        #local variable
        double = total * 2
        print(double)

    double_it()
    return total

#Glocal scope
special = 5

def get_total(a, b):
    #enclosed scope variable declared inside a function
    total = a + b
    print(special)

    def double_it():
        #local variable
        double = total * 2
        print(special)

    double_it()

    return total