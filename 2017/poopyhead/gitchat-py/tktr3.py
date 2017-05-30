# -*- coding: utf-8 -*-
import Tkinter as tk
from tkFont import Font
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from Queue import Queue
import sys

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
            app.notify(event)
        
        
    def on_modified(self, event):
        if event.is_directory:
            return None
        else:
            app.notify(event)
        
        
    def on_moved(self, event):
        if event.is_directory:
            return None
        else:
            app.notify(event)

        

class App(object):
    def __init__(self):
        path = sys.argv[1] if len(sys.argv) > 1 else "./tmp"
        handler = CustomHandler(self)
        self.observer = Observer()
        self.observer.schedule(handler, path, recursive=False)
        self.lineNumber = 0

        self.queue = Queue()
        self.root = tk.Tk()

        self.initMenu()
        self.initUi(path)
        self.observer.start()

    def initUi(self, path):
        myFont = Font(family="Helvetica", size=14)
        
        self.text = tk.Text(self.root)
        self.text.configure(font=myFont)
        self.text.tag_config("red", background="red", foreground="white")
        self.text.pack(fill="both", expand=True)

        self.welcomeMsg = " " * 50 + "Welcome to Gitchat" + " " * 50
        self.text.insert(tk.INSERT, self.welcomeMsg + "\n")
        self.lineNumber = self.lineNumber + 1
        self.text.tag_add("red", str(self.lineNumber) + ".0", str(self.lineNumber) + "." + str(len(self.welcomeMsg)))
        self.text.insert("end", "Watching %s...\n" % path)
        self.text.tag_add("red", "1.0", "1.150")
        self.text.config(state=tk.DISABLED)

        self.root.bind("<Destroy>", self.shutdown)
        self.root.bind("<<WatchdogEvent>>", self.handle_watchdog_event)

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
        #print("event type:", type(watchdog_event))
        #self.text.insert("end", str(watchdog_event.src_path) + "\n")
        self.text.config(state=tk.NORMAL)
        with open(watchdog_event.src_path) as f:
            lines = f.readlines()
            f.close()
            for line in lines:
                self.text.insert("end", line + "\n")
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
