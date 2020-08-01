class Stack:
    def __init__(self):
        self.stack=[]
    # to add
    def add(self,data):
        try:
            if data not in self.stack:
                self.stack.append(data)
                return True
            else:
                return False
        except:
            return "Something went wrong"
    #to view
    def peek(self):
        try:
            return self.stack[-1]
        except:
            return "stack is empty."
    #to remove
    def remove(self):
        try:
            if len(self.stack)<=0:
                return "Stack is empty"
            else:
                return self.stack.pop()
        except:
            return "Something went wrong"

def main():
    print("Options:")
    print("1.View Stack")
    print("2.Add element")
    print("3.Delete element")
    opt=int(input("Enter the operation to be performed: "))
    if(opt==1):
        print(sta.peek())
    elif(opt==2):
        sta.add(input("Enter the element to be added: "))
    elif(opt==3):
        sta.remove()
    else:
        print("enter valid option")
    fo=input("do you want to perform further operations(Yes/No): ")
    if(fo.lower()=="yes"):
        main()
    elif(fo.lower()=="no"):
        print("Bye!")
    else:
        print("enter valid option.")
sta=Stack()
main()