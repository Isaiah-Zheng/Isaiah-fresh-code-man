#這是如何去迭代展示一個二位列表的示範
def main1():
    lis=[
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]
    ]

    for i in lis:
        for j in i:
            print(j)

#這是求出行之和最大值的程序
def main2():
    lis1=[
        [2,4,7],
        [4,1,5],
        [0,6,4]
    ]
    k=0
    a=0
    for i in lis1:
        for j in i:
            k+=j
        if k>=a:
            a=k
        k=0
    print(a)

#這是如何去生成一個隨機矩陣
def main():
    import random
    matrix=[]

    num_row=eval(input("你想打印多少行>"))
    num_column=eval(input("你想打印多少列>"))
    for count1 in range(num_row):
        matrix.append([])
        for count in range(num_column):
            matrix[count1].append(random.randint(1,100))
    print(matrix)
# main()

#編寫一個程序，使得列表中每一個元素都往前移動一個
def lis_shift(lis):
    a=lis[0]
    for i in range(len(lis)-1):

        lis[i]=lis[i+1]
    lis[len(lis)-1]=a
    print(lis)
lis_shift([1,2])


