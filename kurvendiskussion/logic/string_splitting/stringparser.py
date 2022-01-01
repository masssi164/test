from typing import List
import sys


def makeToDic(term:str):
    print("makeToDic")
    returner =[]
    # splitting for spaces 
    spacer =term.split(" ")
    # drop first member to get just the right site of the term
    fx =spacer.pop(0)
    print("right site of the term:",spacer)


def main():
    parser =makeToDic(sys.argv[1])

if __name__ == '__main__':
    main()