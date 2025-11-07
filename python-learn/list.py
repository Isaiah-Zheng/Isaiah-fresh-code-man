#這是如何去迭代展示一個二位列表的示範
import random

from ipykernel.compiler import murmur2_x86
from openpyxl.styles.builtins import total


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
#lis_shift([1,2])

#編寫一個程式，使得一個二維矩陣被打亂，但是保留所有元素的存在
class Matrix:
    import random
    #我們檢測這個矩陣的規模
    def __init__(self,content):
        self.content=content
    def get_size(self):
        # row_num=0
        # column_num=0
        # for row_num in matrix:
        #     row_num+=1

    #很低效，請你用len（）
        row_num=len(self.content)
        column_num=len(self.content[0])
        print(f"我們現在知道了這個矩陣有{row_num}行")
        # for column_num in matrix[0]:
        #     column_num+=1
        print(f"我們現在知道了這個矩陣有{column_num}列")

    def shuffle(self):
#我們需要記住，並瀏覽所有矩陣内容
        row_num=len(self.content)
        column_num=len(self.content[0])
        storage=[]
        for row_in_matrix in self.content :
            for num_in_row in row_in_matrix:
                storage.append(num_in_row)
#我們創造了一個列表去儲存，我們要從其中隨機選一個，并且刪除
        new_matrix=[]
        total=row_num * column_num
        for k in range(row_num):
            new_matrix.append([])
        for row in new_matrix:

            for i in range(column_num):

                random_index = random.randint(0, total-1)            #創造一個能隨機刪除，並儲存的程式
                row.append(storage[random_index])
                del storage[random_index]
                total-=1

        print(new_matrix)

#random.randint(0,row_num*column_num)#這是storage中的隨機編號，包前也包后                                                                      #我們要讓他變成index
                                                                            #storage[random.randint(0,row_num*column_num)]
                                                                             #       random_index=random.randint(0,row_num*column_num)
                                                                            #storage[random_index]

                                                                            #我們要把他輸入到matrix裏面，并且刪除
                                                                            #這個要在for column_num裏循環
                                                                            #new_matrix[0].append(storage[random_index])
                                                                            #del storage[random_index]
a=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

m=Matrix(a)
m.shuffle()














