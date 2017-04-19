# -*- coding: utf-8 -*-


import Tkinter as tk
from tkFont import Font
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from Queue import Queue
import sys
from PIL import Image, ImageTk

class CustomHandler(FileSystemEventHandler):
    def __init__(self, app):
        FileSystemEventHandler.__init__(self)
        self.app = app

        
    def on_created(self, event):
        if event.is_directory:
            return None
        else:
            app.notify(event)
        
        
    def on_deleted(self, event):
        if event.is_directory:
            return None
        else:
            return None
        
        
    def on_modified(self, event):
        if event.is_directory:
            return None
        else:
            app.notify(event)
        
        
    def on_moved(self, event):
        if event.is_directory:
            return None
        else:
            return None

        

class App(object):
    def __init__(self):
        path = sys.argv[1] if len(sys.argv) > 1 else "./messages"
        handler = CustomHandler(self)
        self.observer = Observer()
        self.observer.schedule(handler, path, recursive=False)
        self.lineNumber = 0
        self.previousLine = ""
        self.previousFile = []

        self.queue = Queue()
        self.root = tk.Tk()

        self.initMenu()
        self.initUi(path)
        self.initImages()
        self.observer.start()

    def initUi(self, path):
        myFont = Font(family="Helvetica", size=14)
        
        self.text = tk.Text(self.root)
        self.text.configure(font=myFont)
        self.text.tag_config("secret", background="white", foreground="white")
        self.text.tag_config("white", background="white", foreground="black")
        self.text.tag_config("black", background="black", foreground="white")
        self.text.tag_config("red", background="red", foreground="white")
        self.text.tag_config("yellow", background="yellow", foreground="black")
        self.text.tag_config("green", background="green", foreground="red")
        self.text.tag_config("blue", background="blue", foreground="yellow")
        self.text.tag_config("orange", background="orange", foreground="black")
        self.text.tag_config("pink", background="pink", foreground="blue")
        self.text.tag_config("cyan", background="cyan", foreground="black")
        self.text.tag_config("brown", background="brown", foreground="yellow")
        self.text.tag_config("aquamarine", background="aquamarine", foreground="black")
        self.text.tag_config("purple", background="purple", foreground="cyan")
        self.text.tag_config("honeydew", background="honeydew", foreground="brown")

        self.text.tag_config("rainbow_violet", background="#9400D3", foreground="white")
        self.text.tag_config("rainbow_indigo", background="#4B0082", foreground="pink")
        self.text.tag_config("rainbow_blue", background="#0000FF", foreground="yellow")
        self.text.tag_config("rainbow_green", background="#00FF00", foreground="blue")
        self.text.tag_config("rainbow_yellow", background="#FFFF00", foreground="brown")
        self.text.tag_config("rainbow_orange", background="#FF7F00", foreground="white")
        self.text.tag_config("rainbow_red", background="#FF0000", foreground="yellow")

        self.shrug = """¯\_(ツ)_/¯"""
        self.smile = """【ツ】"""
        
        self.text.pack(fill="both", expand=True)

        self.welcomeMsg = " " * 50 + "Welcome to Gitchat" + " " * 50
        self.lineNumber = self.lineNumber + 1
        self.text.insert(tk.INSERT, self.welcomeMsg + "\n")
        self.text.tag_add("red", str(self.lineNumber) + ".0", str(self.lineNumber) + "." + str(len(self.welcomeMsg)))

        self.lineNumber = self.lineNumber + 1
        self.text.insert("end", "Watching %s...\n" % path)
        self.text.config(state=tk.DISABLED)

        self.root.bind("<Destroy>", self.shutdown)
        self.root.bind("<<WatchdogEvent>>", self.handle_watchdog_event)

    def initImages(self):
        self.images = {}
        
        basewidth = 32
        buf = Image.open('./messages/emojis/creeper.gif')
        wpercent = (basewidth/float(buf.size[0]))
        hsize = int((float(buf.size[1])*float(wpercent)))
        buf = buf.resize((basewidth,hsize), Image.ANTIALIAS)
        self.images['creeper'] = ImageTk.PhotoImage(buf)

        basewidth = 32
        buf = Image.open('./messages/emojis/poo.gif')
        wpercent = (basewidth/float(buf.size[0]))
        hsize = int((float(buf.size[1])*float(wpercent)))
        buf = buf.resize((basewidth,hsize), Image.ANTIALIAS)
        self.images['poo'] = ImageTk.PhotoImage(buf)

        basewidth = 32
        buf = Image.open('./messages/emojis/happy.gif')
        wpercent = (basewidth/float(buf.size[0]))
        hsize = int((float(buf.size[1])*float(wpercent)))
        buf = buf.resize((basewidth,hsize), Image.ANTIALIAS)
        self.images['happy'] = ImageTk.PhotoImage(buf)

        
    def initMenu(self):
        self.root.title("Gitchat-py")
        
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        fileMenu = tk.Menu(menubar)
        fileMenu.add_command(label="Exit", command=self.onExit)
        menubar.add_cascade(label="File", menu=fileMenu)

        helpmenu = tk.Menu(menubar)
        menubar.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="About...", command=self.About)
        
    def handle_watchdog_event(self, event):
        """Called when watchdog posts an event"""
        watchdog_event = self.queue.get()
        
        self.text.config(state=tk.NORMAL)
        with open(watchdog_event.src_path) as f:
            lines = f.readlines()
            f.close()
            self.text.config(state=tk.NORMAL)
            if self.previousFile == lines:
                return None
            else:
                self.previousFile = lines
                for line in lines:
                    parts = line.split(":")
                    if len(parts) == 3:
                        myName = parts[0].strip()
                        myMsg = parts[1].strip()
                        myTag = parts[2].strip().lower()
                    elif len(parts) == 2:
                        myName = parts[0].strip()
                        myMsg = parts[1].strip()
                        myTag = "white"
                    elif len(parts) == 1:
                        myName = "poopsie lala"
                        myMsg = parts[0].strip()
                        myTag = "white"
                    else:
                        myName = "poopsie lala"
                        myMsg = line.strip()
                        myTag = "white"

                    rainbowColors = []
                    rainbowColors.append("rainbow_violet")
                    rainbowColors.append("rainbow_indigo")
                    rainbowColors.append("rainbow_blue")
                    rainbowColors.append("rainbow_green")
                    rainbowColors.append("rainbow_yellow")
                    rainbowColors.append("rainbow_orange")
                    rainbowColors.append("rainbow_red")
                    
                    
                    if myTag == "white" or myTag == "yellow" or myTag == "green" or myTag == "blue" or myTag == "orange" or myTag == "pink" or myTag == "cyan" or myTag == "brown" or myTag == "aquamarine" or myTag == "purple" or myTag == "honeydew":
                        self.lineNumber = self.lineNumber + 1
                        self.text.insert("end", myName + " > " + myMsg + "\n")
                        self.text.tag_add(myTag, str(self.lineNumber) + ".0", str(self.lineNumber) + "." + str(len(myName)))
                                           
                    elif myTag == "rainbow":
                        self.lineNumber = self.lineNumber + 1
                        self.text.insert("end", myName + " > " + myMsg + "\n")
                        nameLen = len(myName)
                        self.text.tag_add("white", str(self.lineNumber) + ".0", str(self.lineNumber) + "." + str(nameLen))
                        idx = 0
                        for character in range(nameLen + 3, len(myMsg) + nameLen, 5):
                            mycolor = rainbowColors[idx]
                            idx = (idx + 1) % len(rainbowColors)                               
                            self.text.tag_add(mycolor, str(self.lineNumber) + "." + str(character), str(self.lineNumber) + "." + str(character + 7))
                    elif myTag == "secret":
                        self.lineNumber = self.lineNumber + 1
                        self.text.insert("end", myName + " > " + myMsg + " <---***Secret Message***" + "\n")
                        nameLen = len(myName)
                        self.text.tag_add("white", str(self.lineNumber) + ".0", str(self.lineNumber) + "." + str(nameLen))
                        self.text.tag_add("secret", str(self.lineNumber) + "." + str(nameLen + 3), str(self.lineNumber) + "." + str(len(myMsg) + nameLen + 3))
                        self.text.tag_add("red", str(self.lineNumber) + "." + str(len(myMsg) + nameLen + 3 + 1), str(self.lineNumber) + "." + str(len(myMsg) + nameLen + 3 + 24))
                    elif myTag == "papaya":
                        self.lineNumber = self.lineNumber + 1
                        self.text.insert("end", myName + " > " + myMsg + "\n")
                        nameLen = len(myName)
                        self.text.tag_add("orange", str(self.lineNumber) + ".0", str(self.lineNumber) + "." + str(nameLen))
                        self.text.tag_add("yellow", str(self.lineNumber) + "." + str(nameLen + 3), str(self.lineNumber) + "." + str(len(myMsg) + nameLen + 3))
                    elif myTag == "pastel":
                        self.lineNumber = self.lineNumber + 1
                        self.text.insert("end", myName + " > " + myMsg + "\n")
                        nameLen = len(myName)
                        self.text.tag_add("pink", str(self.lineNumber) + ".0", str(self.lineNumber) + "." + str(nameLen))
                        self.text.tag_add("aquamarine", str(self.lineNumber) + "." + str(nameLen + 3), str(self.lineNumber) + "." + str(len(myMsg) + nameLen + 3))
                    elif myTag == "shrug":
                        self.lineNumber = self.lineNumber + 3
                        self.text.insert("end", "\n" + myName + " > " + self.shrug + "\n\n")
                    elif myTag == "smile":
                        self.lineNumber = self.lineNumber + 3
                        self.text.insert("end", "\n" + myName + " > " + self.smile + "\n\n")
                    elif myTag == "creeper":
                        self.lineNumber = self.lineNumber + 3
                        self.text.insert("end", "\n" + myName + " > ")
                        self.text.image_create(tk.END,image=self.images['creeper'])
                        self.text.insert("end", "\n\n")
                    elif myTag == "happy":
                        self.lineNumber = self.lineNumber + 3
                        self.text.insert("end", "\n" + myName + " > ")
                        self.text.image_create(tk.END,image=self.images['happy'])
                        self.text.insert("end", "\n\n")
                    elif myTag == "poo":
                        self.lineNumber = self.lineNumber + 3
                        self.text.insert("end", "\n" + myName + " > ")
                        self.text.image_create(tk.END,image=self.images['poo'])
                        self.text.insert("end", "\n\n")
                    else:
                        self.lineNumber = self.lineNumber + 1
                        self.text.insert("end", myName + " > " + myMsg + "\n")
                        self.text.tag_add("white", str(self.lineNumber) + ".0", str(self.lineNumber) + "." + str(len(myName)))

        self.text.config(state=tk.DISABLED)
                            


    def shutdown(self, event):
        """Perform safe shutdown when GUI has been destroyed"""
        self.observer.stop()
        self.observer.join()

    def mainloop(self):
        """Start the GUI loop"""
        self.root.mainloop()

    def notify(self, event):
        """Forward events from watchdog to GUI"""
        self.queue.put(event)
        self.root.event_generate("<<WatchdogEvent>>", when="tail")

    def onExit(self):
        self.quit()

    def About(self):
        print "This is a simple example of a menu"

app = App()
app.mainloop()
