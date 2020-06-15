def gen_fib(n):
    a=1
    b=1
    output= []
    for i in range(n):
        output.append(a)
        a,b=b,a+b
    return output
for number in gen_fib(10):
    print(number)