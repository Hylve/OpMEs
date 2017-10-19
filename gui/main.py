#!/usr/bin/python3
import tkinter as tk
from dnd import DragManager


class MyFirstGUI(tk.Frame):
    def __init__(self, master):

        #wtf?
        super(MyFirstGUI, self).__init__()

        self.tempNode = ""


        self.master = master
        self.master.title("OpMEs GUI")

        self.toplabel = tk.Label(root,text="top label")
        self.toplabel.pack(side="top")

        self.bottomlabel = tk.Label(root,text="bottom label")
        self.bottomlabel.pack(side="bottom")

        self.leftFrame = tk.Frame(root, height=400, width=200, bg="gray")
        self.leftFrame.pack(fill="y", side="left")

        self.canvas = tk.Canvas(root, name="canvas", width=500, height=400, bg="darkgray")
        self.canvas.bind('<Enter>', self.check)
        self.canvas.pack(fill="both", expand=1, side="right")

        self.createWidgets()


    def check(self, event):
        """This function is only for sending check to self.enter"""
        self.enter(event, check=1)

    def enter(self, event, check):
        if (check == 1):
            canvas = event.widget
            print(root.winfo_pointerx() - root.winfo_rootx())
            print(root.winfo_pointerx() - root.winfo_rootx())
            #x = canvas.canvasx(self.tempX) - root.winfo_pointerx()
            #y = canvas.canvasy(self.tempY) - root.winfo_pointery()
            #x = canvas.canvasx(event.x)
            #y = canvas.canvasy(event.y)
            #print("Placed node at",x,y)
        self.tempNode = ""

    def nodeDrop(self, event):
        self.tempX = root.winfo_pointerx() - root.winfo_rootx()
        self.tempY = root.winfo_pointery() - root.winfo_rooty()
        print("tempX",self.tempX)
        print("tempY",self.tempY)

    def addNode(self,event):
        nodesWindow = tk.Toplevel(self)
        nodesWindow.wm_title("New Node")

        node = tk.Button(nodesWindow, text = "Node")
        node.bind('<ButtonRelease-1>', self.nodeDrop)
        node.grid(padx = 3, pady = 2,
                        row = 0, column = 0,
                        sticky = "NW"
                        )

        srcNode = tk.Button(nodesWindow,
            text = "Source Node").grid(padx = 3, pady = 2,
                            row = 1, column = 0,
                            sticky = "NW"
                            )

        destNode = tk.Button(nodesWindow,
            text = "Destination Node").grid(padx = 3, pady = 2,
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
