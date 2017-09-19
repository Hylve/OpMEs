#!/usr/bin/python3
'''
Name: main.py
Devs: Chris [ecn@ecn.se],
Version: 0.0.0.7
Desc:
'''
#
import sys              # To get the current pythonverion
#
from classes.nodeClass import nodeClass                 # import the node class
from classes.flowClass import flowClass                 # import the flow class
from classes.constraintsClass import constraintsClass   # import the constraints class

''' Functions '''
def createNodeFunction(nodeType):
    # IS THIS FUNCTION NEEDED?
    '''
    docs for function
    -----------------
    createNodeFunction("TYPE"), where TYPE is NODE,SOURCE or DESTINATION
    '''
    try:
        if nodeType not in ["SOURCE","DESTINATION","NODE"]:
            raise ValueError("Not a correct node type")

        nodeClass.createNode(nodeType)
    except Exception as e:
        raise

def createFlowFunction(flowType,flowSource, flowDestination):
    '''
    docs for createFlowFunction: This function creates a new flow and append it to the connected nodes.

    Used classes in function: nodeClass, flowClass.
    '''
    try:
        if flowType not in ["INT","FLT"]:
            raise ValueError("Not a correct flow type.")

        flow,flowId = flowClass.createFlow(flowType, flowSource,flowDestination)    # create flow
        nodeClass.nodesDict[flowDestination].addInFlow(flowId)                      # add flow to destination node
        nodeClass.nodesDict[flowSource].addOutFlow(flowId)                          # add flow to source node
    except Exception as e:
        raise

def deleteNodeFunction(nodeId):
    '''
    docs for deleteNodeFunction: This function deletes a node and all flow that is connected to the node.

    Used classes in function: nodeClass, flowClass.
    '''
    try:
        allFlows = []                   # empty list of all flows in the node
        nodesToDeleteIngoingFlows = {}  # create empty dict for nodes that needs to remove ingoing flows from
        nodesToDeleteOutgoingFlows = {} # create empty dict for nodes that needs to remove outgoing flows from

        if nodeClass.nodesDict[nodeId].getInFlows() is not None: # if the node type is not a "SOURCE"
            for item in nodeClass.nodesDict[nodeId].getInFlows():
                allFlows.append(item)

        if nodeClass.nodesDict[nodeId].getOutFlows() is not None:  # if the node type is not a "DESTINATION"
            for item in nodeClass.nodesDict[nodeId].getOutFlows():
                allFlows.append(item)

        for flowId in allFlows:
            nodesToDeleteIngoingFlows[flowClass.flowsDict[flowId].getFlowDestination()]=flowId  # get the ID of the destination node
            nodesToDeleteOutgoingFlows[flowClass.flowsDict[flowId].getFlowSource()]=flowId      # get the ID of the source node
            flowClass.deleteFlow(flowId)                                                        # delete flow

        for nodeIdIn, flowIdIn in nodesToDeleteIngoingFlows.items():
            nodeClass.nodesDict[nodeIdIn].deleteInFlow(flowIdIn) # Remove Destinationflows from NODES that are connected to the flow ID

        for nodeIdOut, flowIdOut in nodesToDeleteOutgoingFlows.items():
            nodeClass.nodesDict[nodeIdOut].deleteOutFlow(flowIdOut) # Remove Ingoingflows from NODES that are connected to the flow ID

        nodeClass.deleteNode(nodeId) # delete the node

    except Exception as e:
        raise
def deleteFlowFunction(flowId):
    '''
    docs for deleteFlowFunction:

    Used classes in function: nodeClass, flowClass.
    '''
    try:
        nodeClass.nodesDict[flowClass.flowsDict[flowId].getFlowDestination()].deleteInFlow(flowId)  # delete flow in destination node
        nodeClass.nodesDict[flowClass.flowsDict[flowId].getFlowSource()].deleteOutFlow(flowId)      # delete flow in source node
        flowClass.deleteFlow(flowId)                                                                # delete flow
    except Exception as e:
        raise

def main():
    problem_name = 'Name'                                   # Name of the problem we want to solve'
    print ("Python version: "+str(sys.version_info[0:4]))   # Prints the current python version

    # EXAMPLES HOW TO USE THE CLASSES READ MORE IN DOCSTRING FOR CLASS:

    print(nodeClass.nodesDict)
    print(flowClass.flowsDict)

    createNodeFunction("NODE") # Node#0
    createNodeFunction("NODE") # Node#1
    createNodeFunction("NODE") # Node#2
    createNodeFunction("NODE") # Node#3
    createNodeFunction("NODE") # Node#4
    print(nodeClass.nodesDict)

    createFlowFunction("INT", 0, 1) # Flow #0
    createFlowFunction("INT", 1, 2) # Flow #1
    createFlowFunction("INT", 2, 3) # Flow #2
    print(nodeClass.nodesDict)
    print(flowClass.flowsDict)


    deleteNodeFunction(2) # delete Node #2
    deleteNodeFunction(3) # delete Node #3
    print(nodeClass.nodesDict)
    print(flowClass.flowsDict)

    createNodeFunction("NODE") # create new node (it's going to be assigned node id 2)
    deleteFlowFunction(0) # delete flow #0
    print(nodeClass.nodesDict)
    print(flowClass.flowsDict)

    createFlowFunction("INT", 0, 1) # create a now flow with the assigned ID #0
    print(nodeClass.nodesDict)
    print(flowClass.flowsDict)


if __name__ == '__main__':
    main()
