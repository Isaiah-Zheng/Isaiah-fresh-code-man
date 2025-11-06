#計算階乘
def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)
#計算斐波那契
def fibonacci(n):
    if n==1 or n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(factorial(3))
print(fibonacci(6))