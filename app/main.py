#!/usr/bin/python3

import sys

<<<<<<< HEAD
#sys.path.append('./frontend')       #To be able to import mainGUI file
#sys.path.append('./backend')       #To be able to import main file
#
import backendMain                                 # import the GUI
=======
sys.path.append('./frontend')       #To be able to import mainGUI file
sys.path.append('./backend')       #To be able to import main file

import backendMain
import mainGUI
>>>>>>> 4175ffe9d5802ad03d0e808abaaead46a13466bb

backendMain.createNodeFunction("SOURCE")
