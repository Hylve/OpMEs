#!/usr/bin/python3
'''
Name: main.py
Devs: Chris [ecn@ecn.se],
Version: 0.0.0.5
Desc:
'''

import sys              # To get the current pythonverion

class nodeClass(object):
    #
    nodesDict = {} # class var place the dictionary here for now?

    """
    docstring for this class
        Attributes:
            id (int): the id of the node.
            namedescription (str):
            type (str): 3 types are should be availible (NODE,SOURCE and DESTINATION)
            inGoingFlows (list):
            outGoingFlows (list):

    An class instance is created dynamically. Therefore a node can be created "on the go". The class have an dictionary as a class variable.
    In the dictionary all the instances is stored. The key in the dictionary is the node ID.


    HOW TO CREATE A NEW NODE:
        nodeClass.createNode("NODE") | call the classmethod on the node class with a specified input argument for the node type.

    HOW TO USE A FUNCTION WITHIN THE CLASS (FOR EXAMPLE changeName):
        nodeClass.nodesDict[nodeId].changeName("New name") |

    """

    @classmethod
    def createNode(cls,nodeType):
        ''' this class method dynamically creates instances (new nodes) '''
        nodeId=len(nodeClass.nodesDict) # use a better implementation of an node ID. What happens if a node is deleted.


        node=nodeClass(nodeId,nodeType)
        cls.nodesDict[nodeId]=node
        return node

    #classmethod to remove an instance

    # Constructor
    def __init__(self, nodeId, nodeType): # add all the inputs in the init method use if statement if the vars is empty
        # implement cost for destination and source node
        self.nodeId         = nodeId
        self.nodeName       = "NODE-"+str(self.nodeId)
        # Move below to subclasses?
        self.nodeType       = nodeType # is this needed here?
        #
        self.inGoingFlows   = None # node node, destination node
        self.outGoingFlows  = None # node node, source node
        self.constraints    = None # node node
        self.cost           = None
        if nodeType == "NODE":
            self.inGoingFlows   = []
            self.outGoingFlows  = []
            self.constraints    = []
        elif nodeType == "SOURCE":
            self.outGoingFlows  = []
            self.cost =[]
        elif nodeType == "DESTINATION":
            self.inGoingFlows  = []
            self.cost =[]

    def __repr__(self):
        '''

        '''
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
        return self.nodeInFlows
    def getOutFlows(self):
        return self.nodeOutFlows
    # Mutator methods (Setters)
    def changeName(self, newName):
        self.nodeName = newName
    def addInFlow(self, inFlowToAdd):
        self.inGoingFlows.append(inFlowToAdd)
    def addOutFlow(self, outFlowToAdd):
        self.outGoingFlows.append(outFlowToAdd)
    # remove inflow function
    # remove outflow function

class sourceNode(nodeClass):
    pass
class destinationNode(nodeClass):
    pass
class nodeNode(nodeClass):
    pass
class childNode(nodeClass):
    pass

class flowClass(object):
    """
    docstring forflowClass
        Attributes:
            flowId
            flowDestionation
            flowSource
            flowType
    """

    flowsDict = {} # set this in subclass?

    @classmethod
    def createFlow(cls,flowType, flowDestination,flowSource):
        ''' this class method dynamically creates instances (new flows) '''
        flowId=len(flowClass.flowsDict) # use a better implementation of an flow ID. What happens if a flow is deleted.
        flow=flowClass(flowId,flowType, flowDestination,flowSource)
        cls.flowsDict[flowId]=flow
        ''' When a new flow is created append flow to node '''
        nodeClass.nodesDict[flowDestination].addInFlow(flowId)
        nodeClass.nodesDict[flowSource].addOutFlow(flowId)

        return flow


    def __init__(self,flowId,flowType,flowDestination,flowSource):
        self.flowId             = flowId
        self.flowType           = flowType
        self.flowName           = "flow-"+str(self.flowId)
        # Below should be in subclasses
        self.flowDestination    = flowDestination
        self.flowSource         = flowSource

    def __repr__(self):
        '''

        '''
        return "flowClass('{}','{}','{}','{}','{}')".format(self.flowId, self.flowType, self.flowName,self.flowDestination, self.flowSource)

    # Accessers methods (Getters)
    def getFlowData (self):
        return self.flowId+self.flowType+self.flowDestination+self.flowSource
    def getFlowId (self):
        return self.flowId
    def getFlowType (self):
        return self.flowType
    def getFlowName (self):
        return self.flowName
    def getFlowDestination (self):
        return self.flowDestination
    def getFlowSoruce (self):
        return self.flowSource
    def getFlowSrcAndDest (self):
        return self.flowDestination,self.flowSource

    # Mutator methods (Setters)
    def changeFlowName (self, newFlowName):
        pass


class intFlow(flowClass):
    pass

class floatFlow(flowClass):
    pass

class constraints(nodeClass):
    '''
    Make this class a subclass of nodeClass?
        Attributes:
    '''
    # Constructor
    def __init__(self):
        pass

    # Accessers methods (Getters)


    # Mutator methods (Setters)


def createNodeFunction(nodeType):
    try:
        nodeClass.createNode(nodeType)
    except Exception as e:
        raise
def createFlowFunction(flowType, flowDestination,flowSource):
    try:
        createFlow(flowType, flowDestination,flowSource)
    except Exception as e:
        raise


def main():
    problem_name = 'Name' # Name of the problem we want to solve'
    print ("Python version: "+str(sys.version_info[0])) # Prints the current python version

    # EXAMPLES HOW TO USE THE NODE CLASS READ MORE IN DOCSTRING FOR CLASS:
    print(nodeClass.nodesDict)
    nodeClass.createNode("NODE")
    print(nodeClass.nodesDict)
    nodeClass.createNode("SOURCE")
    print(nodeClass.nodesDict)
    nodeClass.createNode("DESTINATION")
    print(nodeClass.nodesDict)
    flowClass.createFlow("INT", 0,1)
    print(nodeClass.nodesDict)
    print(flowClass.flowsDict)
    print("---")
    flowClass.flowsDict[0].getFlowSrcAndDest

    #nodeClass.nodesDict[0].changeName("New name")
    #print(nodeClass.nodesDict)
    #nodeClass.nodesDict[0].addInFlow("F1")
    #createNodeFunction("DESTINATION")
    #print(nodeClass.nodesDict)
    #print (help(nodeClass))
    #sourceNode.createNode("SOURCE")
    #print(nodeClass.nodesDict)
    #nodeNode.createNode("NODE")
    #print(nodeClass.nodesDict)


def opti():
    #from pulp import *
    pass

if __name__ == '__main__':
    main()
