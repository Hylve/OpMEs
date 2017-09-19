#!/usr/bin/python3
'''
Name: constraintsClass.py
Devs: Chris [ecn@ecn.se],
Version: 0.0.0.6
Desc:
'''
class constraintsClass(object):
    '''
    Make this class a subclass of nodeClass?
        Attributes:
    '''
    constraintsDict = {}
    possibleConstraints = {'Equals':'=','GreaterThan':'>','LessThan':'<','GreaterOrEqual':'>=','LessOrEqual':'<='}
    # Constructor
    @classmethod
    def createConstraint(cls,nodeId,flowId,constraintType):
        pass
    def __init__(self,nodeId,flowId,constraintType):
        self.nodeId         = nodeId
        self.flowId         = flowId
        self.constraintType = constraintType

    # Accessers methods (Getters)
    def getConstraint(self):
        pass

    # Mutator methods (Setters)
def main():
    print("You are in constraintsClass.py")
    print(constraintsClass.possibleConstraints)
if __name__ == '__main__':
    main()
