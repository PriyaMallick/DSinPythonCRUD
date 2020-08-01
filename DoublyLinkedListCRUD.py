class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
        self.previous= None

class doubly_linkedlist:
    def __init__(self):
        self.head=None;

    # create node
    def create(self):
        try:
            a = int(input("enter the value: "))
            newlist.head = Node(a)
            return newlist
        except:
            print("something went wrong")

    # view
    def view(self):
        try:
            view1 = self.head
            li=list()
            while (view1 is not None):
                li.append(view1.data)
                view1 = view1.next
            print(li)
        except:
            print("no elements in the linked list")

    # addnode
    def addnode(self):
        try:
            print("1.Beginning")
            print("2.Middle")
            print("3.End")
            pos = int(input("enter the position: "))

            def beginning():
                newd = input("enter the value: ")
                newnode = Node(newd)
                newnode.next = self.head
                if self.head is not None:
                    self.head.previous=newnode
                self.head=newnode
                print("node added")

            def middle():
                newd2 = input("enter the value: ")
                newnode2 = Node(newd2)
                p=newlist.head.next
                if p is None:
                    return
                newnode2.next = p.next
                p.next = newnode2
                newnode2.previous = p
                if newnode2.next is not None:
                    newnode2.next.previous = newnode2
                print("node added")

            def end():
                newd1 = input("enter the value: ")
                newnode1 = Node(newd1)
                if self.head is None:
                    self.head = newnode1
                    return
                temp = self.head
                while (temp.next is not None):
                    temp = temp.next
                temp.next = newnode1
                newnode1.previous=temp
                print("node added")

            if pos == 1:
                beginning()
            elif pos == 2:
                middle()
            elif pos == 3:
                end()
            else:
                print("enter valid option")
        except:
            print("something went wrong")

    # delete
    def delete(self):
        try:
            dele=input("enter the element to be deleted: ")
            n = self.head
            if self.head.next is None:
                if self.head.data == dele:
                    self.head = None
                else:
                    print("Item not found")
                return

            if self.head.data == dele:
                self.head = self.head.next
                self.head.previous = None
                return

            while n.next is not None:
                if n.data == dele:
                    break;
                n = n.next
            if n.next is not None:
                n.previous.next = n.next
                n.next.previous = n.previous
            else:
                if n.data == dele:
                    n.previous.next = None
            print("node deleted")

        except:
            print("linked list underflow")

def main():
    try:
        print("Operations:")
        print("1.Create Node")
        print("2.View LinkedList")
        print("3.Add node")
        print("4.Delete node")
        opt=int(input("enter the operation to be performed: "))
        if(opt==1):
            newlist.create()
        elif (opt==2):
            newlist.view()
        elif (opt==3):
            newlist.addnode()
        elif (opt==4):
            newlist.delete()
        else:
            print("Invalid option")
        i=input("do u want to perform more operation? Y/N: ")
        if (i.lower()=="y"):
            main()
        elif(i.lower()=="n"):
            print("bye!")
        else:
            print("enter valid option.")
    except:
        print("something went wrong")
newlist = doubly_linkedlist()
main()