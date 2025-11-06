
def main():
    class Rectangle:
        def __init__(self,length=1,width=2):
            self.length=length
            self.width=width
        def get_area(self):
            return self.length*self.width
    a=Rectangle(2,3)
    b=Rectangle()
    area=a.get_area()
    print(f"長方形的面積是{area}")
    print(b.length,b.width)
main()
