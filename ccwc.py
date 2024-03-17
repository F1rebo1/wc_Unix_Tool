import argparse

def getWords(fileName):
    wordCount = 0
    with open(fileName,"r") as file:
        for line in file:
            line = line.split()
            for words in line:
                wordCount += 1

    return wordCount


def getLines(fileName):
    lineCount = 0
    with open(fileName,"r") as file:
        for line in file:
            lineCount += 1
    
    return lineCount

def getBytes(fileName):
    byteCount = 0
    with open(fileName,"r") as file:
        for line in file:
            byteCount += len(line)

    
    return byteCount

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', dest="fileName", type=str)
    parser.add_argument('-l', dest="fileName", type=str)
    parser.add_argument('-w', dest="fileName", type=str)

    args = parser.parse_args()
    fileName = args.fileName

    print(str(getBytes(fileName)) + " " + str(fileName))
    print(str(getLines(fileName)) + " " + str(fileName))
    print(str(getWords(fileName)) + " " + str(fileName))

if __name__ == "__main__":
    main()