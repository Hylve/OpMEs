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
    node1=nodeModule.node("1","NodeOne","Node",["in1","in2"],["out1"])
    print node1
    # Below is for testing for testing
    print(node1.getName())
    node1.changeName("NewNodeName")
    print node1
    node1.addInFlow("new inflow")
    print node1
    node1.addOutFlow("new outflow")
    print node1

    a=node1.getAll()
    #print a
    print type(a)




if __name__ == '__main__':
    main()
