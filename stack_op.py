import array

# same as que except stack class you can use que
class Stack:
    def __init__(self):
        self.my_self = array.array('i',[])

    def is_empty(self):
        if len(self.my_self):
            return False
        else:
            return True
        
    def push(self, element):
        self.my_self.append(element)

    def pop(self):
        if self.is_empty():
            print("you can't stack pop")
        else:
            self.my_self.pop()

if __name__ == "main":
    stack = Stack() #object create
 
    stack.push(1)
    stack.push(2)
    stack.push(3)

    print(stack.my_self)
    
