#!/usr/bin/env python3

#Name: Dave Loper
#Class: THEA 1713
#Date: Fall 2021
#Project: New Original Method
#Source Code: Copyright Dave Lper 2021 APGL 3.0+

# Import Libraries
import tkinter as tk
#from tkinter import Variable, ttk, messagebox, filedialog, scrolledtext
from tkinter import *
from tkinter import ttk, messagebox, filedialog
import time
import re 
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
scripttext=[]
targetCharacter=""
debug = 1



class PreprocFrame(ttk.Frame):
    def __init__(self, parent):
        # Place all functions up top
        # Frame Operations
        def printToConsole():
            print(self.stMainText.get("1.0","end-1c"))

 #       def addSelectedToConsole():
 #           try:
 #               selected = self.stMainText.get(SEL_FIRST,SEL_LAST)
 #               print(selected)
 #           except:
 #               messagebox.showinfo(title="Selection Error", message="Try selecting some text")
                

        def listjoin(listvariable):
            output='\n'.join(listvariable)
            return output

        def cleanWhiteSpace():
            input = self.stMainText.get("1.0","end-1c")
            output=[]
            linesremoved = 0
            for line in input.split("\n"):
                if (line == "") or (line == "\r") or (re.search(r'$.^', line)):
                    linesremoved = linesremoved + 1
                else:
                    output.append(line)
            output1=listjoin(output)
            self.stMainText.delete("1.0","end-1c")
            self.stMainText.insert(tk.INSERT, output1)
            if debug == 1:
                self.stDebugText.delete("1.0","end-1c")
                self.stDebugText.insert(tk.INSERT, "Lines Removed: " + str(linesremoved))
            if targetCharacter != "":
                applyHighlight(targetCharacter)
                
        def removeStartsWith():
            global targetCharacter
            try:
                input = self.stMainText.get("1.0","end-1c")
                output=[]
                linesremoved = 0
                selected = self.stMainText.get(SEL_FIRST,SEL_LAST)
                myregex = r"^" + re.escape(selected)
                if debug == 1:
                    self.stDebugText.delete("1.0","end-1c")
                    self.stDebugText.insert(tk.INSERT, "Selected Text: " + str(selected))
                for line in input.split("\n"):
                    if re.search(myregex, line):
                        linesremoved = linesremoved + 1
                    else:
                        output.append(line)
                output1=listjoin(output)
                self.stMainText.delete("1.0","end-1c")
                self.stMainText.insert(tk.INSERT, output1)
                if debug == 1:
                    self.stDebugText.delete("1.0","end-1c")
                    self.stDebugText.insert(tk.INSERT, "Lines Removed: " + str(linesremoved))
                if targetCharacter != "":
                    applyHighlight(targetCharacter)


            except:
                messagebox.showinfo(title="Selection Error", message="Try selecting some text")

#            return output

        def addSelectedChar():
            global targetCharacter
            try:
                selected = self.stMainText.get(SEL_FIRST,SEL_LAST)
                varCharacters.append(selected)
                self.stUtilityText.delete("1.0","end-1c")
                self.stUtilityText.insert(tk.INSERT, listjoin(varCharacters))
                if debug == 1:
                    self.stDebugText.delete("1.0","end-1c")
                    self.stDebugText.insert(tk.INSERT, varCharacters)
            except:
                messagebox.showinfo(title="Selection Error", message="Try selecting some text")
            if targetCharacter != "":
                myregex = r"^\s*?" + selected
                myregex1 = r"^\s*?" + targetCharacter
                input = self.stMainText.get("1.0","end-1c")
                output=[]
                linesremoved = 0
                nonematch = 0
                marker = 0
                if debug == 1:
                    self.stDebugText.delete("1.0","end-1c")
                    self.stDebugText.insert(tk.INSERT, "myregex: " + str(myregex))
                for line in input.split("\n"):
                    if re.search(myregex, line):
                        marker = 1
                        nonematch = 1
                    else:
                        nonematch = 0
                    if re.search(myregex1, line):
                        marker = 0
                        nonematch = 1
                    if marker == 1:
                        linesremoved = linesremoved + 1
                    elif marker == 0:
                        output.append(line)
                output1=listjoin(output)
                self.stMainText.delete("1.0","end-1c")
                self.stMainText.insert(tk.INSERT, output1)
                if targetCharacter != "":
                    applyHighlight(targetCharacter)

#                if debug == 1:
#                    self.stDebugText.delete("1.0","end-1c")
#                    self.stDebugText.insert(tk.INSERT, "Lines Removed: " + str(linesremoved))
                

        def removeString():
            global targetCharacter
            start = self.tbDelRangeStart.get("1.0","end-1c")
            end = self.tbDelRangeEnd.get("1.0","end-1c")
            myregex = re.escape(start) + r"([^" + re.escape(end) + r"])*" + re.escape(end)
#            if debug == 1:
#                self.stDebugText.delete("1.0","end-1c")
#                self.stDebugText.insert(tk.INSERT, myregex)
            input = self.stMainText.get("1.0","end-1c")
            output=[]
            linesremoved = 0
            nonematch = 0
            marker = 0
            if debug == 1:
                self.stDebugText.delete("1.0","end-1c")
                self.stDebugText.insert(tk.INSERT, "myregex: " + str(myregex))
            if debug == 1:
                self.stDebugText.delete("1.0","end-1c")
            for line in input.split("\n"):
                if re.search(myregex, line):
                    if debug == 1:
                        self.stDebugText.insert(tk.INSERT, line + "\n")
                    line = re.sub(myregex, "", line)
                    linesremoved = linesremoved + 1
                output.append(line)
            output=listjoin(output)
            self.stMainText.delete("1.0","end-1c")
            self.stMainText.insert(tk.INSERT, output)
#            if debug == 1:
#                self.stDebugText.delete("1.0","end-1c")
#                self.stDebugText.insert(tk.INSERT, "Items Removed: " + str(linesremoved))
            self.tbDelRangeEnd.delete("1.0","end-1c")
            self.tbDelRangeStart.delete("1.0","end-1c")         
            if targetCharacter != "":
                applyHighlight(targetCharacter)

        def applyHighlight(targetCharacter):
            if "highlight" in self.stMainText.tag_names():
                self.stMainText.tag_delete("highlight")
            i = len(targetCharacter)
            idx = "1.0"
            while True:
                idx = self.stMainText.search(targetCharacter, idx, nocase=1, stopindex='end')
                if idx:
                    idx2 = self.stMainText.index("%s+%dc" % (idx, i))
                    self.stMainText.tag_add("highlight", idx, idx2)
                    self.stMainText.tag_config("highlight", background="yellow")
                    idx = idx2
                else: return


        def addTargetChar():
            global targetCharacter
            try:
                selected = self.stUtilityText.get(SEL_FIRST,SEL_LAST)
                self.tbTargetChar.delete("1.0","end-1c")
                self.tbTargetChar.insert(tk.INSERT, selected)
                targetCharacter = selected
                if debug == 1:
                    self.stDebugText.delete("1.0","end-1c")
                    self.stDebugText.insert(tk.INSERT, targetCharacter)
            except:
                messagebox.showinfo(title="Selection Error", message="Try selecting some text")

            try:
                applyHighlight(targetCharacter)
            except:
                pass

        def purgeCharacter(i,input):
            myregex = re.escape(i)
            output=[]
            for line in input.split("\n"):
                if re.search(myregex, line):
                    line = re.sub(myregex, " ", line)
                output.append(line)
            return output

        def finalizeScript():
            global targetCharacter
            applyHighlight(targetCharacter)
            myregex = re.escape(targetCharacter)
            if debug == 1:
                self.stDebugText.delete("1.0","end-1c")
                self.stDebugText.insert(tk.INSERT, myregex)
            input = self.stMainText.get("1.0","end-1c")
            output=[]
            linesremoved = 0
            for line in input.split("\n"):
                if re.search(myregex, line):
#                    if debug == 1:
#                        self.stDebugText.insert(tk.INSERT, line + "\n")
                    line = re.sub(myregex, "", line)
                    linesremoved = linesremoved + 1
                output.append(line)
            # Loop through punctuation removals
            output=listjoin(output)
            for i in {",", ".", ";", ":", "?", "!", "--", ",\n", ".\n", ";\n", "!\n", "?\n", ":\n", ",\r", ".\r", ";\r", "!\r", "?\r", ":\r"}:
                input = output
                output = purgeCharacter(i,input)
                output=listjoin(output)
            self.stMainText.delete("1.0","end-1c")
            self.stMainText.insert(tk.INSERT, output)
            if targetCharacter != "":
                applyHighlight(targetCharacter)

        # File operations
        # File explorer dialog window for existing files
        def browseFiles():
            global FILENAME
            global scripttext
            # Get our filename
            FILENAME = filedialog.askopenfilename(initialdir = ".", title = "Select a File", filetypes = (("TXT files","*.txt*"),("all files","*.*")))
            # This pushes our variable to the debug box
            if debug == 1:
                self.stDebugText.delete("1.0","end-1c")
                self.stDebugText.insert(tk.INSERT, FILENAME)
            scripttext = languageanalysis.read_file(FILENAME)
            text=listjoin(scripttext)
            self.stUtilityText.delete("1.0","end-1c")
            self.tbTargetChar.delete("1.0","end-1c")
            self.tbDelRangeStart.delete("1.0","end-1c")
            self.tbDelRangeEnd.delete("1.0","end-1c")
            self.stMainText.delete("1.0","end-1c")
            self.stMainText.insert(tk.INSERT, text)
            varCharacters=[]
            targetCharacter=""            
            return scripttext

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
                        text="Script Preprocessor",
                        bd=5, anchor=W)
        titleLabel.pack(side=LEFT)

        # MID FRAME
        midFrame = Frame(root, width=1350, height=50)
        midFrame.pack(side=TOP, expand=1, anchor=N)
        # Scroll Text: Script
        self.stMainText = scrolledtext.ScrolledText(midFrame,wrap=tk.WORD,width=100,height=20)
        self.stMainText.pack(side=LEFT)
        # Scroll Text: Characters
        utilityFrame = Frame(root, width=350, height=50)
        utilityFrame.pack(side=TOP, expand=1, anchor=N)
        labelShowUtility = Label(utilityFrame, font=('arial', 10, 'bold'),
                        text="Character List",
                        bd=5, anchor=W)
        labelShowUtility.pack(side=LEFT)
        self.stUtilityText = scrolledtext.ScrolledText(utilityFrame,wrap=tk.WORD,width=15,height=10)
        self.stUtilityText.pack(side=LEFT)
        # Text Box: Target Character
        midsubFrame = Frame(utilityFrame, width=1000, height=2)
        midsubFrame.pack(side=TOP, expand=1, anchor=N)
        labelShowMain = Label(midsubFrame, font=('arial', 10, 'bold'),
                        text="Target Character",
                        bd=5, anchor=N)
        labelShowMain.pack(side=LEFT)
        self.tbTargetChar = Text(
                        midsubFrame,
                        height=1,
                        width=15)
        self.tbTargetChar.pack(side=LEFT)

        midsubFrame1 = Frame(utilityFrame, width=1000, height=2)
        midsubFrame1.pack(side=TOP, expand=1, anchor=N)
        labelDelRangeStart = Label(midsubFrame1, font=('arial', 10, 'bold'),
                        text="Delete From",
                        bd=5, anchor=W)
        labelDelRangeStart.pack(side=LEFT)
        self.tbDelRangeStart = Text(
                        midsubFrame1,
                        height=1,
                        width=2)
        self.tbDelRangeStart.pack(side=LEFT)
        labelDelRangeEnd = Label(midsubFrame1, font=('arial', 10, 'bold'),
                        text="To",
                        bd=5, anchor=W)
        labelDelRangeEnd.pack(side=LEFT)
        self.tbDelRangeEnd = Text(
                        midsubFrame1,
                        height=1,
                        width=2)
        self.tbDelRangeEnd.pack(side=LEFT)


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
        buttonSaveText = tk.Button(Bottom,text="Save Text Analysis",command=createFiles
            ).pack(side=LEFT)
#        buttonDebugChar = tk.Button(Bottom,text="debug Selected Character",command=addSelectedToConsole
#            ).pack(side=LEFT)
        buttonAddChar = tk.Button(Bottom,text="Add Selected Character",command=addSelectedChar
            ).pack(side=LEFT)
        buttonRemoveStartsWith = tk.Button(Bottom,text="Add Target Character",command=addTargetChar
            ).pack(side=LEFT)
        buttonWhiteSpace = tk.Button(Bottom,text="Vacuum Whitespace",command=cleanWhiteSpace
            ).pack(side=LEFT)
        buttonRemoveStartsWith = tk.Button(Bottom,text="Remove lines: Start with selected",command=removeStartsWith
            ).pack(side=LEFT)
        buttonRemoveFromTo = tk.Button(Bottom,text="Remove item: From/To",command=removeString
            ).pack(side=LEFT)
        buttonFinalize = tk.Button(Bottom,text="Finalize",command=finalizeScript
            ).pack(side=LEFT)
        # Debug button
#        if debug == 1:
#            buttonDebug = tk.Button(Bottom,text="Debug",command=toggleDebug
#                ).pack(side=LEFT)

#        self.stMainText.insert(tk.INSERT, scrollboxtext())



if __name__ == "__main__":
    root = tk.Tk()
    root.title("Play Script Analyzer")
    root.state("zoomed")
    root.configure(bg="grey80")
    PreprocFrame(root)
    root.mainloop()
