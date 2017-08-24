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




if __name__ == '__main__':
    main()
