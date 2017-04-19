from Tkinter import *
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

mainloop()



##from Tkinter import *
##
##root = Tk()
##
##listbox = Listbox(root)
##listbox.pack()
##
##for i in range(20):
##    listbox.insert(END, str(i))
##
##mainloop()
