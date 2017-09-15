#!/usr/bin/python3
'''
Name:
Desc:
Author:
Version:
'''
import main             #
import setupModule      #
import nodeModule       # node data

class createNode(object):
    """docstring for """
    # Constructor
    def __init__(self):
        pass
    # Accessers methods (Getters)

    # Mutator methods (Setters
    def newNode(self,newNodeType):
        # check hom many existing nodes there is

        # get the lates node tag and add 1 to it (counter)
        # (self, id, namedescription,type,inGoingFlows,outGoingFlows)
        '''
        idTag type is int   - get from a list that contains all nodedata
        idName is str       - get from a list that contains all nodedata


        '''
        #idTag = 1
        #idName=str(idTag)
        #creates a new node with default settings
        #idName=nodeModule.node(idTag,str(idTag),type,[],[])
        print("newnode - here")
        print(newNodeType)

def main():
    pass

if __name__ == '__main__':
    main()
