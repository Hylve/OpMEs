#!/usr/bin/python3
import tkinter as tk
from dnd import DragManager


class MyFirstGUI(tk.Frame):
    def __init__(self, master):

        #wtf?
        super(MyFirstGUI, self).__init__()

        self.tempNode = None


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
        self.canvas.pack(fill="both", expand=1, side="right")

        self.createWidgets()

    def enter(self, event, check):
        if (check == 1 and self.tempNode != None):
            canvasX = self.tempX - 110
            canvasY = self.tempY - 20
            canvas = event.widget
            canvas.create_oval(canvasX-20, canvasY-20, canvasX+20, canvasY+20, fill=self.color)
        self.tempNode == None


    def nodeDrop(self, event, node, color):
        self.tempX = root.winfo_pointerx() - root.winfo_rootx()
        self.tempY = root.winfo_pointery() - root.winfo_rooty()
        if not(self.tempY < 20 or self.tempY > 380 or self.tempX < 110 or self.tempX > 600):
            self.check = 1
            self.color = color
            self.tempNode = node
            print("node name:", node)
        else:
            self.check = 0

    def addNode(self,event):
        nodesWindow = tk.Toplevel(self)
        nodesWindow.wm_title("New Node")

        node = tk.Button(nodesWindow, text = "Node")
        node.bind('<ButtonRelease-1>', lambda event, node="normal", color="blue": self.nodeDrop(event, node, color))
        node.grid(padx = 3, pady = 2,
                        row = 0, column = 0,
                        sticky = "NW"
                        )

        srcNode = tk.Button(nodesWindow, text = "Source Node")
        srcNode.bind('<ButtonRelease-1>', lambda event, node="source", color="red": self.nodeDrop(event, node, color))
        srcNode.grid(padx = 3, pady = 2,
                            row = 1, column = 0,
                            sticky = "NW"
                            )

        destNode = tk.Button(nodesWindow, text = "Destination Node")
        destNode.bind('<ButtonRelease-1>', lambda event, node="destination",color="green": self.nodeDrop(event, node, color))
        destNode.grid(padx = 3, pady = 2,
                            row = 2, column = 0,
                            sticky = "NW"
                            )

        #dnd = DragManager()
        #dnd.add_dragable(node)


    def createWidgets(self):
        self.nodeButton = tk.Button(self.leftFrame,  activebackground="darkgray",
                             text = "New Node")
        self.nodeButton.bind('<Button-1>', self.addNode)
        self.nodeButton.grid(row = 0, column = 0, pady = 2, padx = 10, sticky = "N")



root = tk.Tk()
#root.minsize(300,300)
#Resolution , x drawing point, y drawing point. x and  drawing point not needed.
width = 600
height = 400
root.geometry("600x400+100+100")
my_gui = MyFirstGUI(root)
my_gui.mainloop()
