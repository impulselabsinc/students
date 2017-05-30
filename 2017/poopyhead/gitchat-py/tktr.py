from Tkinter import *
from tkFileDialog   import askopenfilename

def NewFile():
    print "New File!"
def OpenFile():
    name = askopenfilename()
    print name
def About():
    print "This is a simple example of a menu"

root = Tk()
text = Text(root)
text.pack()
text.config(state=DISABLED)
text.config(state=NORMAL)
text.insert(INSERT, "Hello.....")
text.config(state=DISABLED)
text.config(state=NORMAL)
text.insert(END,"\n"+ "yeah!")

text.tag_add("yellow", "1.0", "1.4")
text.tag_add("black", "2.0", "2.3")
text.tag_config("yellow", background="yellow", foreground="blue")
text.tag_config("black", background="black", foreground="white")
text.config(state=DISABLED)

menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open...", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)

mainloop()

