#!/usr/bin/python3

import sys              # To get the current pythonverion

import tkinter as tk

sys.path.append('./backend')
from classes.nodeClass import nodeClass                 # import the node class

class MyFirstGUI(tk.Frame):
    def __init__(self, master):
        #wtf?
        super(MyFirstGUI, self).__init__()
        self.movement = 0
        self.tempCounter= 1
        self.nodeType = None
        self.tempNode = None
        self.nodeMenu = None


        self.master = master
        self.master.title("OpMEs GUI")

        self.toplabel = tk.Label(root,text="top label")
        self.toplabel.pack(side="top")

        self.bottomlabel = tk.Label(root,text="bottom label")
        self.bottomlabel.pack(side="bottom")

        self.leftFrame = tk.Frame(root, height=400, width=200, bg="gray")
        self.leftFrame.pack(fill="y", side="left")


        self.canvas = tk.Canvas(root, name="canvas", width=500, height=400, bg="darkgray")
        self.canvas.bind('<Enter>', lambda event, check = 1: self.enter(event, check))
        self.canvas.bind('<Button-3>', self.displayNodeMenu)
        self.canvas.bind('<ButtonRelease-1>', self.setMovement)
        self.canvas.pack(fill="both", expand=1, side="right")
        self.createWidgets()

    def setMovement(self, event):
        if self.movement == 1:
            print("The node was moved to:",event.x, event.y)
            self.canvas.unbind('<B1-Motion>')
            self.movement = 0

    def displayNodeMenu(self, event):
        if (self.nodeMenu != None):
            self.nodeMenu.destroy()
        try:
            nodeID = event.widget.gettags("current")[0]
        except:
            print("There is nothing there, add an object.")
        else:
            self.nodeMenu = tk.Menu(self.canvas, tearoff=0)
            self.nodeMenu.add_command(label="Move node", command=lambda: self.moveClick(nodeID))
            self.nodeMenu.add_command(label="Edit node", command=lambda: self.editNode(nodeID))
            self.nodeMenu.add_command(label="Delete node", command=lambda: self.deleteNode(nodeID))
            x = root.winfo_pointerx()# - root.winfo_rootx()
            y = root.winfo_pointery()# - root.winfo_rooty()
            self.nodeMenu.post(x, y)

    def moveClick(self, nodeID):
        self.canvas.bind('<B1-Motion>', lambda event: self.moveNode(event, nodeID))
        self.movement = 1

    def moveNode(self, event, nodeID):
        obj = event.widget.gettags("current")[0]
        if obj == nodeID:
            newX = event.x - self.tempX
            newY = event.y - self.tempY
            self.canvas.move(nodeID, newX, newY)
            self.tempX = event.x
            self.tempY = event.y

    def editNode(self, nodeID):
        print("EDIT ---:",nodeID)

    def deleteNode(self, nodeID):
        print("nodeType is:",nodeID)
        self.canvas.delete(nodeID)

    def enter(self, event, check):
        if (check == 1 and self.nodeType != None):
            canvas = event.widget
            path = './frontend/images/' + self.nodeType + '.png'
            self.photo = tk.PhotoImage(file = path)
            self.tempNode = nodeClass.createNode(self.nodeType, self.photo, self.tempX, self.tempY)
            print("added node:",self.tempNode, "          ", "nodeId:", self.tempNode.nodeId)
            canvas.create_image(event.x, event.y, image = self.photo, tags = self.tempCounter)
            self.tempCounter += 1
        self.nodeType = None


    def nodeDrop(self, event, node):
        self.tempX = root.winfo_pointerx() - root.winfo_rootx()-110  #this is the width of self.leftFrame.
        self.tempY = root.winfo_pointery() - root.winfo_rooty()-20 #the height of toplabel
        if not(self.tempY < 0 or self.tempY > 360 or self.tempX < 0 or self.tempX > 490):
            print("node",node)
            self.check = 1
            self.nodeType = node
        else:
            self.check = 0

    def addNode(self,event):
        nodesWindow = tk.Toplevel(self)
        nodesWindow.resizable(width=False, height=False)
        nodesWindow.wm_title("New Node")

        node = tk.Button(nodesWindow, text = "Normal node")
        node.bind('<ButtonRelease-1>', lambda event, node="NODE": self.nodeDrop(event, node))
        node.grid(padx = 3, pady = 2,
                        row = 0, column = 0,
                        sticky = "NW"
                        )

        srcNode = tk.Button(nodesWindow, text = "Source node")
        srcNode.bind('<ButtonRelease-1>', lambda event, node="SOURCE": self.nodeDrop(event, node))
        srcNode.grid(padx = 3, pady = 2,
                            row = 1, column = 0,
                            sticky = "NW"
                            )

        destNode = tk.Button(nodesWindow, text = "Destination node")
        destNode.bind('<ButtonRelease-1>', lambda event, node="DESTINATION": self.nodeDrop(event, node))
        destNode.grid(padx = 3, pady = 2,
                            row = 2, column = 0,
                            sticky = "NW"
                            )


    def createWidgets(self):
        self.nodeButton = tk.Button(self.leftFrame,  activebackground="darkgray",
                             text = "New Node")
        self.nodeButton.bind('<Button-1>', self.addNode)
        self.nodeButton.grid(row = 0, column = 0, pady = 2, padx = 10, sticky = "N")


if __name__ == '__main__':
    root = tk.Tk()
    #root.minsize(300,300)
    #Resolution , x drawing point, y drawing point. x and  drawing point not needed.
    width = 600
    height = 400
    root.geometry("600x400+100+100")
    my_gui = MyFirstGUI(root)
    my_gui.mainloop()
