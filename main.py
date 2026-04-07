piecesList= ["♜", "♞", "♝","♛" ,"♚" ,"♝" ,"♞", "♜","♟" ,"♟" ,"♟", "♟", "♟" ,"♟", "♟", "♟"]

chessBoard=["♜", "♞", "♝","♛" ,"♚" ,"♝" ,"♞", "♜",
            "♟" ,"♟" ,"♟", "♟", "♟" ,"♟", "♟", "♟",
            "·","·","·",".","·","·","·","·",
            "·","·","·","·","·","·","·","·",
            "·","·","·","·","·","·","·","·",
            "·","·","·","·","·","·","·","·",
            "p" ,"p" ,"p", "p", "p" ,"p", "p", "p",
            "r", "n", "b","q" ,"k" ,"b" ,"n", "r",
            ]
chessBoardNum = [
    1, 2,   3, 4,  5,   6, 7,  8,
    9, 10, 11, 12, 13, 14, 15, 16,
    17, 18, 19, 20, 21, 22, 23, 24,
    25, 26, 27, 28, 29, 30, 31, 32,
    33, 34, 35, 36, 37, 38, 39, 40,
    41, 42, 43, 44, 45, 46, 47, 48,
    49, 50, 51, 52, 53, 54, 55, 56,
    57, 58, 59, 60, 61, 62, 63, 64
]

chessBoardVal = [
    "8a","8b","8c","8d","8e","8f","8g","8h",
    "7a","7b","7c","7d","7e","7f","7g","7h",
    "6a","6b","6c","6d","6e","6f","6g","6h",
    "5a","5b","5c","5d","5e","5f","5g","5h",
    "4a","4b","4c","4d","4e","4f","4g","4h",
    "3a","3b","3c","3d","3e","3f","3g","3h",
    "2a","2b","2c","2d","2e","2f","2g","2h",
    "1a","1b","1c","1d","1e","1f","1g","1h"
]


for i in range (0,64,8): #goes (start,stop,step)
    print(chessBoard[i:i+8]) #go from 0->9 but doesn't do 9 only 8

transList=[8,8]

#def inputToChess(input,chessboard,transList):
    #nothing=1

whiteMoveSelect=input("White Move Select: ")
#whiteMoveSelect=list(whiteMoveSelect)
print(whiteMoveSelect)
whiteMove=input("White Move: ")
#whiteMove=list(whiteMove)
print(whiteMove)


def findIndexPlacement(chessBoardVals,whiteMove):
    index=0
    for each in chessBoardVals:
        if chessBoardVals==(whiteMove):
            return index
        index=index+1


print (findIndexPlacement(chessBoardVal,whiteMove))


