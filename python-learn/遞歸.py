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

#你一直在位這個github做了一些時間的浪費，不要再這樣了。
#你一直在位這個github做了一些時間的浪費，不要再這樣了。你終於知道去改默認分支了