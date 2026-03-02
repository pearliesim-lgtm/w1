class Rect:
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def calculate_perimeter(self):
        return 2*(self.length+self.width)
    
l=int(input("enter length of rectangle:"))
w=int(input("Enter the width of rectangle:"))
u=(input("enter unit:"))
obj=Rect(l,w)
result=obj.calculate_perimeter()
print("Perimeter of Rectangle:",result)
print(u)