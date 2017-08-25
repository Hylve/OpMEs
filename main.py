#!/usr/bin/python3
'''
Name: main.py
Desc:
Author: Chris [ecn@ecn.se]
Version: 0.0.0.2
'''
import nodeModule # node data
import setupModule #
import sys





class mainClass(object):
    """docstring for this class """
    # Constructor
    def __init__(self):
        pass
    # Accessers methods (Getters)

    # Mutator methods (Setters)


def main():
    print ("Python version: "+str(sys.version_info[0]))
    setupModule.setupModel() #

if __name__ == '__main__':
    main()
