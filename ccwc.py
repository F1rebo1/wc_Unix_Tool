import sys
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
    parser.add_argument('file_name', nargs='?', type=str, help='The name of the file to process')
    parser.add_argument('-c', dest="c", action='store_true')
    parser.add_argument('-l', dest="l", action='store_true')
    parser.add_argument('-w', dest="w", action='store_true')
    parser.add_argument('-m', dest="m", action='store_true')

    args = parser.parse_args()
    c = args.c
    l = args.l
    w = args.w
    m = args.m

    if not args.file_name:
        if sys.stdin:
            with open("newFile.txt","w") as file:
                for line in sys.stdin:
                    file.write(line)
            fileName = "newFile.txt"
            if args.c:
                chCnt = getChars(fileName)
                print(f'{chCnt} {fileName}')
            elif args.l:
                lnCnt = getLines(fileName)
                print(f'{lnCnt} {fileName}')
            elif args.w:
                wcCnt = getWords(fileName)
                print(f'{wcCnt} {fileName}')
            elif args.m:
                bytCnt = getBytes(fileName)
                print(f'{bytCnt} {fileName}')
    elif args.file_name:
        fileName = args.file_name
        wcCnt,chCnt,lnCnt = getWords(fileName),getChars(fileName),getLines(fileName)
        print(f'{lnCnt} {wcCnt} {chCnt} {fileName}')
    elif c:
        fileName = c
        chCnt = getChars(fileName)
        print(f'{chCnt} {fileName}')
    elif l:
        fileName = l
        lnCnt = getLines(fileName)
        print(f'{lnCnt} {fileName}')
    elif w:
        fileName = w
        wcCnt = getWords(fileName)
        print(f'{wcCnt} {fileName}')
    elif m:
        fileName = m
        bytCnt = getBytes(fileName)
        print(f'{bytCnt} {fileName}')

if __name__ == "__main__":
    main()