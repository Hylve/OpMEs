'''
Name: main.py
Desc: Main
Author: Chris [ec@ecn.se]
Version: 0.0.0.1
'''
import nodeModule



class node(object):
    """docstring for this class """
    # Constructor
    def __init__(self):
        pass
    # Accessers methods (Getters)

    # Mutator methods (Setters)


def main():
    #create new node
    node1=nodeModule.node("1","NodeOne","Node",["in1","in2"],["out1"])
    #print new node
    print node1
    # Below is for testing 
    print(node1.getName())#prints the name of the node
    node1.changeName("NewNodeName")# changes the node name
    print node1 # print node
    node1.addInFlow("new inflow") # adds a new flow
    print node1 #print node
    node1.addOutFlow("new outflow") # adds a new flow
    print node1 #print node

    a=node1.getAll() # recive all data from node
    #print a 
    print type(a) #print type (tuple)




if __name__ == '__main__':
    #if this is the main-file run main function
    main()
