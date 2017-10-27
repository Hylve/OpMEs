#!/usr/bin/python3
'''
Name: nodeClass.py
Devs: Chris [ecn@ecn.se],
Version: 0.0.0.7
Desc:
'''
class nodeClass(object):
    """
    docstring for this class
        Attributes:
            nodeId (int): the id of the node.
            nodeName (str): the name of the node.
            nodeType (str): 3 node types availible (NODE,SOURCE and DESTINATION).
            inGoingFlows (list): the nodes ingoing flows.
            outGoingFlows (list): the nodes outgoing flows.
            constraints (list): the nodes constraints
            cost (list): the nodes costs.

    An class instance is created dynamically. Therefore a node can be created "on the go". The class have an dictionary as a class variable.
    In the dictionary all the instances is stored. The key in the dictionary is the node ID and the value in the dictionary is the instance itself.

    HOW TO CREATE A NEW NODE:
        nodeClass.createNode("NODE") | call the classmethod on the node class with a specified input argument for the node type.

    HOW TO USE A FUNCTION WITHIN THE CLASS (FOR EXAMPLE changeName):
        nodeClass.nodesDict[nodeId].changeName("New name") |
    """
    nodesDict = {}          # a dictionary that stores all node instances
    deletedNodesList = []   # a list that contains all deleted node IDs

    @classmethod
    def createNode(cls,nodeType, picture=None, x=None, y=None):
        ''' this class method dynamically creates instances (new nodes) '''
        if not cls.deletedNodesList: # if there is no deleted nodes
            nodeId=len(nodeClass.nodesDict) # set node ID to the lenght to of the node dictionar
        else: # if there is deleted nodes
            cls.deletedNodesList.sort() #sort the list
            nodeId=cls.deletedNodesList[0] # set node id to the lowest ID (first in sorted)
            cls.deletedNodesList.pop(0) #remove first item in list


        node=nodeClass(nodeId,nodeType, picture, x,y) # createa node instance
        cls.nodesDict[nodeId]=node # append created instance to dictionary
        return node

    @classmethod
    def deleteNode(cls,nodeId):
        ''' this class method delete an existing node instance in the dictionary that stores all the instances. '''
        cls.nodesDict.pop(nodeId,None) # Delete the nod
        cls.deletedNodesList.append(nodeId) # Append the deleted nodes ID to a list

    # Constructor
    def __init__(self, nodeId, nodeType, picture, x, y): # add all the inputs in the init method use if statement if the vars is empty
        self.picture        = picture                   # set node picture.
        self.nodeId         = nodeId                    # set node ID.
        self.nodeName       = "NODE-"+str(self.nodeId)  # set the default node name to "NODE-nodeID".
        self.yCoord         = y                         # Y coordinate.
        self.xCoord         = x                         # X coordinate.
        # Move below to subclasses?
        self.nodeType       = nodeType                  # set node type.
        self.inGoingFlows   = None                      # valid for: destination node.
        self.outGoingFlows  = None                      # valid for: source node.
        self.constraints    = None                      # valid for: node node.
        self.cost           = None                      # valid for: node node.
        if nodeType == "NODE": # If the node type is "NODE"
            self.inGoingFlows   = []
            self.outGoingFlows  = []
            self.constraints    = []
        elif nodeType == "SOURCE": # if the node type is source
            self.outGoingFlows  = []
            self.cost           = []
        elif nodeType == "DESTINATION": # if the node type is destination
            self.inGoingFlows   = []
            self.cost           = []


    def __repr__(self):
        return "nodeClass('{}','{}','{}','{}','{}','{}','{}')".format(self.nodeId, self.nodeName, self.nodeType,self.inGoingFlows, self.outGoingFlows, self.constraints, self.cost)

    # Accessers methods (Getters)
    def getAll(self):
        return self.nodeId,self.nodeName,self.nodeType,self.inGoingFlows,self.outGoingFlows
    def getId(self):
        return self.nodeId
    def getName(self):
        return self.nodeName
    def getType(self):
        return self.nodeType
    def getInFlows(self):
        return self.inGoingFlows
    def getOutFlows(self):
        return self.outGoingFlows
    def getCosts(self):
        return self.cost

    # Mutator methods (Setters)
    def changeName(self, newName):
        self.nodeName = newName
    def changeNameToDefault(self):
        self.nodeName = "NODE-"+str(self.nodeId)
    def addInFlow(self, inFlowToAdd):
        self.inGoingFlows.append(inFlowToAdd)
    def addOutFlow(self, outFlowToAdd):
        self.outGoingFlows.append(outFlowToAdd)
    def deleteInFlow(self,inFlowToDelete):
        self.inGoingFlows.remove(inFlowToDelete)
    def deleteOutFlow(self, outFlowToDelete):
        self.outGoingFlows.remove(outFlowToDelete)

class sourceNode(nodeClass):
    pass
class destinationNode(nodeClass):
    pass
class nodeNode(nodeClass):
    pass

def main():
    print("You are in nodeClass.py")

if __name__ == '__main__':
    main()
