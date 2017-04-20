# -*- coding: utf-8 -*-
import Tkinter as tk
import ttk as ttk
from tkFont import Font
from collections import namedtuple

class MinecraftFrame(ttk.Frame):
    def __init__(self, parent):
        mcFrame = ttk.Frame(parent, width=200, height=100,)
        mcFrame.pack()

        # Add the frame to the notebook
        parent.add(mcFrame, text="Minecraft")

        # Buttons
        b1 = tk.Button(mcFrame, text='postToChat', command=self.mcchat)
        b1.grid(row = 1, column = 4, padx = 5, pady = 5)

        # Text
        global mctxtVar
        mctxtVar = tk.StringVar() #message text input box
        mcmesgtext = tk.Entry(mcFrame, textvariable=mctxtVar)
        mcmesgtext.grid(row = 1, column = 2,) # text for post to chat

    def mcchat(self):
        print  mctxtVar.get()
