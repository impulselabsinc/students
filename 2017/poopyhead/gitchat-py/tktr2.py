#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import *
from tkFont import Font
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class GitChatUi(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)   
        self.parent = parent        
        self.initUI()
        
        
    def initUI(self):
        self.parent.title("Gitchat-py")
        
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Exit", command=self.onExit)
        menubar.add_cascade(label="File", menu=fileMenu)
        
        helpmenu = Menu(menubar)
        menubar.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="About...", command=self.About)

        text = Text(self.parent)
        myFont = Font(family="Helvetica", size=14)
        text.configure(font=myFont)
        text.pack()
        text.insert(INSERT, "Welcome to Gitchat ")
        text.tag_config("red", background="red", foreground="white")
        text.tag_add("red", "1.0", "1.50")
        text.config(state=DISABLED)
        

    def onExit(self):
        self.quit()


    def About(self):
        print "This is a simple example of a menu"

        
class Watcher:
    DIRECTORY_TO_WATCH = "./"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print "Error"

        self.observer.join()



class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            print "Received created event - %s." % event.src_path
            with open(event.src_path) as f:
                lines = f.readlines()
            for line in lines:
                print line

        elif event.event_type == 'modified':
            # Taken any action here when a file is modified.
            print "Received modified event - %s." % event.src_path

def main():
    
    root = Tk()
    root.geometry("500x800+100+100")
    app = GitChatUi(root)
    w = Watcher()
    w.run(app)
    root.mainloop()  


if __name__ == '__main__':
    main()    
