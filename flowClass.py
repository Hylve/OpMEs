#!/usr/bin/python3
'''
Name: flowClass.py
Devs: Chris [ecn@ecn.se],
Version: 0.0.0.6
Desc:
'''
class flowClass(object):
    """
    docstring forflowClass
        Attributes:
            flowId (int): the id of the flow
            flowType (str): the type of the flow, can be integer (INT) or float (FLT).
            flowSource (int): the node id where the flow is pointing to.
            flowDestionation (int): the node id where the flow came from.

    An class instance is created dynamically. Therefore a flow can be created "on the go". The class have an dictionary as a class variable.
    In the dictionary all the instances is stored. The key in the dictionary is the flow ID.

    HOW TO USE A FUNCTION WITHIN THE CLASS:
    flowClass.flowsDict[flowId].getFlowName()
    """


    flowsDict = {} # a dictionary that stores all flow instances
    deletedFlowsList = [] # a list that contains all deleted flow IDs

    @classmethod
    def createFlow(cls,flowType, flowSource,flowDestination):
        ''' this class method dynamically creates instances (new flows) '''
        if not cls.deletedFlowsList:
            flowId=len(flowClass.flowsDict) # use a better implementation of an flow ID. What happens if a flow is deleted.
        else:
            cls.deletedFlowsList.sort()
            flowId=cls.deletedFlowsList[0]
            cls.deletedFlowsList.pop(0)

        flow=flowClass(flowId,flowType, flowSource,flowDestination) # create instance
        cls.flowsDict[flowId]=flow # append instance to dictionary
        return flow, flowId


    @classmethod
    def deleteFlow(cls,flowId):
        cls.flowsDict.pop(flowId,None)

    def __init__(self,flowId,flowType,flowSource,flowDestination):
        self.flowId             = flowId
        self.flowType           = flowType
        self.flowName           = "flow-"+str(self.flowId)
        self.flowNickname       = self.flowType+"-"+str(self.flowId)
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
    def getFlowSource (self):
        return self.flowSource
    def getFlowSrcAndDest (self):
        return self.flowDestination,self.flowSource

    # Mutator methods (Setters)
    def changeFlowName (self, newFlowName):
        self.flowName = newFlowName



class intFlow(flowClass):
    pass

class floatFlow(flowClass):
    pass

def main():
    print("You are in flowClass.py")

if __name__ == '__main__':
    main()
