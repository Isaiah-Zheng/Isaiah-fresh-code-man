class TV:
    def __init__(self):
        self.volume=1
        print(f"the ini volume is {self.volume},you can change it")

    def set_volume(self,volume):
        self.volume=volume
        print(f"the new volume is {self.volume}")

my_TV=TV()
new_volume=int(input("please set a new volume>"))
my_TV.set_volume(new_volume)