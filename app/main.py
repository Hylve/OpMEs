#!/usr/bin/python3

import sys

sys.path.append('./frontend')       #To be able to import mainGUI file
sys.path.append('./backend')       #To be able to import main file

import backendMain
import mainGUI

backendMain.createNodeFunction("SOURCE")
