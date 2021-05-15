def sum(*args):
    result=0
    for value in args:
        result=result+value
    return result
s=sum(10,20,30)
print(s/3)
