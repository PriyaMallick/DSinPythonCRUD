class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class linkedlist:
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
            print("something went wrong")

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
                self.head = newnode
                print("node added")

            def middle():
                newd2 = input("enter the value: ")
                newnode2 = Node(newd2)
                mid_node=self.head.next
                if mid_node is None:
                    print("Node not present")
                    return
                newnode2.next=mid_node.next
                mid_node.next=newnode2
                print("node added")

            def end():
                newd1 = input("enter the value: ")
                newnode1 = Node(newd1)
                if self.head is None:
                    self.head = newnode1
                    return
                temp = self.head
                while (temp.next):
                    temp = temp.next
                temp.next = newnode1
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
            global prev
            dele=input("enter the element to be deleted: ")
            h = self.head
            if (h is not None):
                if h.data ==dele:
                    self.head = h.next
                    h = None
                    return
            while (h is not None):
                if h.data ==dele:
                    break
                prev = h
                h = h.next
            if (h == None):
                return
            prev.next = h.next
            h = None
            print("Node element")
        except:
            print("something went wrong")

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
newlist = linkedlist()
main()