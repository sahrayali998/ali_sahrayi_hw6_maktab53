
def fib(num):
    a = 0
    b = 1
    for i in range(2, num + 1):
        c = a + b
        a = b
        b = c
        if b > num:
            break
        yield b


fibo = fib(9)
for i in fibo:
    print(i, end=" ")