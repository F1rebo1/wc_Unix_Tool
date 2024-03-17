import argparse

def getChars(fileName):
    charCount = 0
    with open(fileName,"rb") as file:
        for line in file:
            charCount += len(line.decode())
    file.close()

    return charCount

def getWords(fileName):
    wordCount = 0
    with open(fileName,"r") as file:
        for line in file:
            line = line.split()
            for words in line:
                wordCount += 1
    file.close()

    return wordCount


def getLines(fileName):
    lineCount = 0
    with open(fileName,"r") as file:
        for line in file:
            lineCount += 1
    file.close()

    return lineCount

def getBytes(fileName):
    byteCount = 0
    with open(fileName,"rb") as file:   #Need to open with rb to read as binary
        for line in file:
            byteCount += len(line)
    file.close()

    return byteCount

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', dest="fileName", type=str)
    parser.add_argument('-l', dest="fileName", type=str)
    parser.add_argument('-w', dest="fileName", type=str)
    parser.add_argument('-m', dest="fileName", type=str)

    args = parser.parse_args()
    fileName = args.fileName

    print(str(getBytes(fileName)) + " " + str(fileName))
    print(str(getLines(fileName)) + " " + str(fileName))
    print(str(getWords(fileName)) + " " + str(fileName))
    print(str(getChars(fileName)) + " " + str(fileName))

if __name__ == "__main__":
    main()