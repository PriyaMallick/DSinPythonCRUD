class Queue:
    def __init__(self):
        self.queue=list()

    #view
    def viewq(self):
        try:
            li=list()
            for i in self.queue:
                li.append(i)
            li.reverse()
            print(li)
        except:
            print("Queue is empty")
    #add element
    def addelement(self,data):
        try:
            self.queue.insert(0,data)
            print("Added")
            return True
        except:
            print("Something went wrong")
    #remove element
    def remove(self):
        try:
            if len(self.queue)>0:
                return self.queue.pop()
        except:
            return "Queue is empty"

def main():
    print("Options:")
    print("1.Add element")
    print("2.Delete element")
    print("3.View queue")
    opt=int(input("Enter the operation to be performed: "))
    if(opt==1):
        q.addelement(input("Enter the element to be added: "))
    elif(opt==2):
        q.remove()
    elif (opt==3):
        q.viewq()
    else:
        print("enter valid option")
    fo=input("do you want to perform further operations(Y/N): ")
    if(fo.lower()=="y"):
        main()
    elif(fo.lower()=="n"):
        print("Bye!")
    else:
        print("enter valid option.")
q=Queue()
main()