'''
Name: nodeModule.py
Desc: The node class
Author: Chris[ecn@ecn.se],
Version: 0.0.0.1
'''

class node(object):
    """docstring for this class """
    # Constructor
    def __init__(self, id, name,type,inGoingFlows,outGoingFlows):
        self.nodeId = id
        self.nodeName = name
        self.nodeType= type
        self.nodeInFlows = inGoingFlows
        self.nodeOutFlows = outGoingFlows
    # Accessers methods (Getters)
    def getAll(self):
        return self.nodeId,self.nodeName,self.nodeType,self.nodeInFlows,self.nodeOutFlows
    def getId(self):
        return self.nodeId
    def getName(self):
        return self.nodeName
    def getType(self):
        return self.nodeType
    def getInFlows(self):
        return self.nodeInFlows
    def getInflows(self):
        return self.nodeOutFlows
    # Mutator methods (Setters)
    def changeName(self, newName):
        self.nodeName = newName
    def addInFlow(self, inFlowToAdd):
        self.nodeInFlows.append(inFlowToAdd);
    def addOutFlow(self, outFlowToAdd):
        self.nodeOutFlows.append(outFlowToAdd);



    def __str__(self):
        '''
        Move string converter? Is it needed in the future?
        '''
        if type(self.nodeInFlows) is list:
            inFlowstr = ''
            for element in self.nodeInFlows:
                inFlowstr += str(element)+";"
            #return inFlowstr
        if type(self.nodeOutFlows) is list:
            outFlowstr = ''
            for element in self.nodeOutFlows:
                outFlowstr += str(element)+";"

        return self.nodeId+";"+self.nodeName+";"+self.nodeType+";"+inFlowstr+outFlowstr

def main():
    # Nothing here will be run.


if __name__ == '__main__':
    main()
