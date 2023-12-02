import re
import numpy as np


def readFile(PathFile):
    with open(f"../lecture1/{PathFile}") as file_text:
        txt = file_text.read()

    txt = re.split("\.", txt)
    txt.remove('')
    txt = [t.replace(",", "") for t in txt]
    splitText = [re.split("\s", t.strip().lower()) for t in txt]
    return splitText

def numberLetter(txt):
    c = 0
    for row in splitText:
        c = c + row.count(txt)
    return c

def caculatorIFIDF(splitText):
    IDF = []
    IF = []
    for row in splitText:
        tempIDF = []
        tempIF = []
        for t in row:
            tempIDF.append(np.log((len(splitText) + 1) / (numberLetter(t) + 1)))
            tempIF.append(row.count(t) / len(row))
        IDF.append(tempIDF)
        IF.append(tempIF)
    

def main():
    splitText = readFile("text.txt")
    caculatorIFIDF(splitText)
    

if __name__ == "__main__":
    main()