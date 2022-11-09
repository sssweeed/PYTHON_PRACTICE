a = input()
def hiFunction(name):
    return("Hi, " + name)
print(hiFunction(a))


a = int(input())
b = int(input())
def sum(x, y):
    return(x + y)
print(sum(a, b))


x = int(input())
def isEven(x):
    if x % 2 == 0:
        return "true"
    else:
        return "false"
print(isEven(x))


x = int(input())
def apples(x):
    return "i have", x, "apples"
print(apples(x))


x = int(input())
def getPower(x):
    return x ** 2
print(getPower(x))
