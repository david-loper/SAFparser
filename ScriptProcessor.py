#!/usr/bin/env python3

#Name: Dave Loper
#Class: THEA 1713
#Date: Fall 2021
#Project: New Original Method: ScriptProcessor
#Source Code: Copyright Dave Lper 2021 APGL 3.0+

# Import Libraries
import tkinter as tk
#from tkinter import Variable, ttk, messagebox, filedialog, scrolledtext
from tkinter import *
from tkinter import ttk, messagebox, filedialog
import time
import re 
import nltk
from importlib import reload
#import tkinter
#from tkinter.constants import RIGHT, W
# work with OS files
import os
from tkinter import scrolledtext
from typing_extensions import Concatenate
# Import my main program as a library
from txtproc import languageanalysis

# Set global variables
varCharacters=[]
FILENAME=""
FILENAMEA=""
scripttext=[]
scripttext1=[]
scripttexta=[]
scripttexta1=[]
targetCharacter=""
debug = 0



class ProcFrame(ttk.Frame):
    def __init__(self, parent):
        def listjoin(listvariable):
            output='\n'.join(listvariable)
            return output

        def linespaces(count):
            for i in range(count,0,-1):
                self.stMainText.insert(tk.INSERT, "\n")
                self.stMainTexta.insert(tk.INSERT, "\n")

        def lexical_density(text):
            return "Lexical Density: " + str(round(len(set(text)) / len(text) * 100,1)) + " %"

        def characterName(FILE):
            myregex = "\/(?:.(?!\/))+$"
            return "Character: " + str(re.findall(myregex,FILE))
#            short = "Character:" + str(re.findall(myregex,FILE))
#            return short

        def flushPalette():
            self.stMainText.delete("1.0","end-1c")
            self.stMainTexta.delete("1.0","end-1c")
        
        def wordCount(text):
            count = "Number of words: " + str(len(text))
            return count
        
        def word_set(text):
            fdist = nltk.FreqDist(text)
            return fdist.most_common(30)
        
        def to_lower(text):
            newlist = []
            for i in text:
                i=i.lower()
                newlist.append(i)
            return newlist

        def list_freq(freqdistribution,freqdistribution1):
            for line in freqdistribution:
                self.stMainText.insert(tk.INSERT, line)
                self.stMainText.insert(tk.INSERT, "\n")
            for line in freqdistribution1:
                self.stMainTexta.insert(tk.INSERT, line)
                self.stMainTexta.insert(tk.INSERT, "\n")

                


        def analyzeAndCompare():
            global scripttext1
            global scripttexta1
            global FILENAME
            global FILENAMEA
            scripttext1 = to_lower(scripttext1)
            scripttexta1 = to_lower(scripttexta1)
            sFILENAME = characterName(FILENAME)
            sFILENAMEA = characterName(FILENAMEA)
            words = wordCount(scripttext1)
            words1 = wordCount(scripttexta1)
            lex = lexical_density(scripttext1)
            lex1 = lexical_density(scripttexta1)
            freqdistribution = word_set(scripttext1)
            freqdistribution1 = word_set(scripttexta1)



            flushPalette()
            self.stMainText.insert(tk.INSERT, sFILENAME)
            self.stMainTexta.insert(tk.INSERT, sFILENAMEA)
            linespaces(2)
            self.stMainText.insert(tk.INSERT, words)
            self.stMainTexta.insert(tk.INSERT, words1)
            linespaces(2)
            self.stMainText.insert(tk.INSERT, lex)
            self.stMainTexta.insert(tk.INSERT, lex1)
#            linespaces(2)
#            self.stMainText.insert(tk.INSERT, freqdistribution)
#            self.stMainTexta.insert(tk.INSERT, freqdistribution1)
            linespaces(2)
            list_freq(freqdistribution,freqdistribution1)
            

        # File operations
        # File explorer dialog window for existing files
        def browseFiles():
            global FILENAME
            global scripttext
            global scripttext1
            # Get our filename
            FILENAME = filedialog.askopenfilename(initialdir = ".", title = "Select a File", filetypes = (("TXT files","*.txt*"),("all files","*.*")))
            scripttext = languageanalysis.read_file(FILENAME)
            scripttext1 = []
            for line in scripttext:
                result = line.split()
                for i in result:
                    scripttext1.append(i)

            # This pushes our variable to the debug box
            if debug == 1:
                self.stDebugText.delete("1.0","end-1c")
                self.stDebugText.insert(tk.INSERT, FILENAME)
                self.stDebugText.insert(tk.INSERT,scripttext1)
            text=listjoin(scripttext)
            self.stMainText.delete("1.0","end-1c")
            self.stMainText.insert(tk.INSERT, text)
            return scripttext1






        # File operations
        # File explorer dialog window for existing files
        def browseFilesa():
            global FILENAMEA
            global scripttexta
            global scripttexta1
            # Get our filename
            FILENAMEA = filedialog.askopenfilename(initialdir = ".", title = "Select a File", filetypes = (("TXT files","*.txt*"),("all files","*.*")))
            scripttexta = languageanalysis.read_file(FILENAMEA)
            scripttexta1 = []
            for line in scripttexta:
                result = line.split()
                for i in result:
                    scripttexta1.append(i)
            # This pushes our variable to the debug box
            if debug == 1:
                self.stDebugText.delete("1.0","end-1c")
                self.stDebugText.insert(tk.INSERT, FILENAMEA)
                self.stDebugText.insert(tk.INSERT,scripttexta1)
            text=listjoin(scripttexta)
            self.stMainTexta.delete("1.0","end-1c")
            self.stMainTexta.insert(tk.INSERT, text)
            return scripttexta1













        # File explorer dialog window for new file
        def createFiles():
            global FILENAME
            # Make a new filename
            FILE_NAME = filedialog.asksaveasfile(initialdir = ".", title = "Create Natural Language File...", defaultextension=".txt", filetypes = (("TXT files","*.txt*"),("all files","*.*")))
            # Get the string version
            FILENAME = os.path.realpath(FILE_NAME.name)
            # Write out the zero'd ledger
            #lines=self.stMainText()
            #lines=scrolledtext.ScrolledText(root)
            lines = self.stMainText.get("1.0","end-1c")
            languageanalysis.write_file(lines,FILENAME)



        ## Define out frames
        topFrame = Frame(root, width=1350, height=50)  # Added "container" Frame.
        topFrame.pack(side=TOP, fill=X, expand=1, anchor=N)

        # TOP FRAME
        titleLabel = Label(topFrame, font=('arial', 20, 'bold'),
                        text="Script Processor",
                        bd=5, anchor=W)
        titleLabel.pack(side=LEFT)
        # MID FRAME
        midFrame = Frame(root, width=1350, height=50)
        midFrame.pack(side=TOP, expand=1, anchor=N)
        # Scroll Text: Script
        self.stMainText = scrolledtext.ScrolledText(midFrame,wrap=tk.WORD,width=50,height=20)
        self.stMainText.pack(side=LEFT)
        self.stMainTexta = scrolledtext.ScrolledText(midFrame,wrap=tk.WORD,width=50,height=20)
        self.stMainTexta.pack(side=LEFT)


        # Debugging Frame
        if debug ==1:
            debugFrame = Frame(root, width=1350, height=50)
            debugFrame.pack(side=TOP, expand=1, anchor=N)
            self.stDebugText = scrolledtext.ScrolledText(debugFrame,wrap=tk.WORD,width=100,height=10)
            self.stDebugText.pack(side=BOTTOM)
        # Bottom Frame
        Bottom = Frame(root, width=1350, height=100, bd=4, relief="ridge")
        Bottom.pack(side=BOTTOM, fill=X, expand=1, anchor=S)
        # Bottom Buttons
        buttonLoadScript = tk.Button(Bottom,text="Load Script",command=browseFiles
            ).pack(side=LEFT)
#        buttonSaveText = tk.Button(Bottom,text="Save Text Analysis",command=createFiles
#            ).pack(side=LEFT)
        buttonTopWords = tk.Button(Bottom,text="Analyze and Compare",command=analyzeAndCompare
            ).pack(side=BOTTOM)
        

        # Debug button
#        if debug == 1:
#            buttonDebug = tk.Button(Bottom,text="Debug",command=toggleDebug
#                ).pack(side=LEFT)
        buttonLoadScripta = tk.Button(Bottom,text="Load Script",command=browseFilesa
            ).pack(side=RIGHT)



if __name__ == "__main__":
    root = tk.Tk()
    root.title("Play Script Language Analyzer")
    root.state("zoomed")
    root.configure(bg="grey80")
    ProcFrame(root)
    root.mainloop()
