#!/usr/bin/env python3
# text processor for language analysis

# Copyright 2021 Dave Loper
#Class: THEA 1713
#Date: Dec 2021
# This code is Open Source Software licensed under the AGPL 3.0+ license.

# Perform our imports

# Test file
FILENAME="Pygmalion.txt"

# Setup our class
class languageanalysis():
# Find the character names in the text

# Split the text by character names

# Purge directions from text

# Display full text

    # Read in text
    def read_file(txtfile):
        # Initialize an empty list
        text = []
        # open up the file and auto close
        with open(txtfile, newline="", encoding="utf-8") as file:
            # define reader object
            #reader = text.readline(file)
            # read out our rows as variables
            for row in file:
        #        print(row.rstrip())
                text.append(row)
            # I need this variable list back in the main menu every time
            return text

    # Our write function. pull in the sales var
    def write_file(lines,FILENAME):
        # open up the file for writing with auto close
        with open(FILENAME, "w", newline="", encoding="utf-8") as file:
#            for line in lines:
            file.write(lines)
#                file.write('\n')


    def main():
        """
        Developement command line debugger
        """
        fulltext = languageanalysis.read_file(FILENAME)
        print("Done")


# Call the main function for local execution.
if __name__ == "__main__":
    languageanalysis.main()

