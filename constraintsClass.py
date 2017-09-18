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
    def __init__(self):
        pass

    # Accessers methods (Getters)


    # Mutator methods (Setters)
def main():
    print(constraintsClass.possibleConstraints)
if __name__ == '__main__':
    main()
