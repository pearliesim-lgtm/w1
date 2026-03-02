class Emp:
    def __init__(self):
        print('Employee class created')

    def __del__(self):
        print("Destructor called to delete class")

def objfun():
    print('Object created')
    obj=Emp()
    print("Object function end ")
    return obj

print('Calling Function')
obj=objfun()
print('Program end')