class Stack:
    def __init__(self):
        self.stack=[]
    #view stack
    def views(self):
        try:
            li = list()
            for i in self.stack:
                li.append(i)
            li.reverse()
            for j in li:
                print(j)
        except:
            print("stack in empty")
    # to add
    def add(self,data):
        try:
            self.stack.append(data)
            return ("Added")
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
    try:
        print("Options:")
        print("1.View top element")
        print("2.Add element")
        print("3.Delete element")
        print("4.View stack")
        opt=int(input("Enter the operation to be performed: "))
        if(opt==1):
            print(sta.peek())
        elif(opt==2):
            sta.add(input("Enter the element to be added: "))
        elif(opt==3):
            sta.remove()
        elif (opt == 4):
            sta.views()
        else:
            print("enter valid option")
        fo=input("do you want to perform further operations(Yes/No): ")
        if(fo.lower()=="yes"):
            main()
        elif(fo.lower()=="no"):
            print("Bye!")
        else:
            print("enter valid option.")
    except:
        print("something went wrong")
sta=Stack()
main()