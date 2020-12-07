# Othello by Harald Wörl (2020)
# ein Brettspiel für zwei Personen - wird auch "Reversi" genannt

# die KI importieren
import sys
import KI_Othello
import numpy as np
import os

def getNewBoard():
    # erstellt eine neue Datenstruktur für die Grundstellung
    board = []
    for x in range(0,9):                                      # die Spalten
        board.append([])
        for y in range(0,9):                                  # die Reihen
            if x == 3 and y == 4 or x == 4 and y == 3:
                board[x].append("X")
                KI_Othello.R[x][y] = -500
            elif x == 3 and y == 3 or x == 4 and y == 4:
                board[x].append("O")
                KI_Othello.R[x][y] = -500
            else:
                board[x].append('.')                         # leere Felder
    return board

def getTestBoard():
    # erstellt eine neue Datenstruktur für die Teststellung
    # hier wird eine bestimmte Stellung vorgegeben
    board = []  # legt eine leere Liste an
    for x in range(0,9):                                    # die Spalten (0 bis 7)
        board.append([])
        for y in range(0,9):                                  # die Zeilen
            if x == 5 and y == 2 or x == 3 and y == 3 or x == 0 and y == 1 or  x == 3 and y == 4 or x == 4 and y == 5 or x == 7 and y == 1 or x == 1 and y == 2 or x == 2 and y == 3 or x == 5 and y == 6 or x == 6 and y == 7:
                board[x].append("X")
                KI_Othello.R[x][y] = -500
            elif x == 3 and y == 5 or x == 4 and y == 4 or x == 4 and y == 3 or x == 4 and y == 2 or x == 5 and y == 1 or x == 6 and y == 1:
                board[x].append("O")
                KI_Othello.R[x][y] = -500
            else:
                board[x].append('.')                         # leere Felder
    return board

def drawBoard(board):
    # Zeichnet die Datenstruktur des Spielfeldes
    # Gibt die Beschriftung am oberen Spielbrettrand aus
    print('  ' + ('01234567'))

    # Gibt die 8 Zeilen aus
    for zeilen in range(len(board)-1):
        # Erstellt den String für eine Zeile auf dem Brett
        boardRow = ''
        # Gibt die 8 Spalten aus (0-7)
        for spalten in range(len(board)-1):
            boardRow += board[spalten][zeilen]
        print('%s %s %s' %(zeilen, boardRow, zeilen)) # das Brett wird gezeichnet

    # Gibt die Beschriftung am unteren Rand des Spielbretts aus
    print('  ' + ('01234567'))

def pruefeGueltigenSpielerZug(board, pos_x, pos_y):
    xmax = 8
    ymax = 8
    xmin = 0
    ymin = 0
    if pos_x < xmin or pos_x > xmax or pos_y < ymin or pos_y > ymax:  # Zug ist außerhalb des Bretts
        print("Ungültiger Zug")
        spielerZieht(board,start)
        return
    if board[pos_x][pos_y] == spieler or board[pos_x][pos_y] == cpu:  # Feld ist besetzt
        print("Ungültiger Zug")
        spielerZieht(board,start)
        return
    try:
        if board[pos_x + 1][pos_y] == cpu and board[pos_x + 2][pos_y] == spieler or \
            board[pos_x + 1][pos_y] == cpu and board[pos_x + 2][pos_y] == cpu and board[pos_x + 3][pos_y] == spieler or \
            board[pos_x + 1][pos_y] == cpu and board[pos_x + 2][pos_y] == cpu and board[pos_x + 3][pos_y] == cpu and \
            board[pos_x + 4][pos_y] == spieler or \
            board[pos_x + 1][pos_y] == cpu and board[pos_x + 2][pos_y] == cpu and board[pos_x + 3][pos_y] == cpu and \
            board[pos_x + 4][pos_y] == cpu and board[pos_x + 5][pos_y] == spieler or \
            board[pos_x + 1][pos_y] == cpu and board[pos_x + 2][pos_y] == cpu and board[pos_x + 3][pos_y] == cpu and \
            board[pos_x + 4][pos_y] == cpu and board[pos_x + 5][pos_y] == cpu and board[pos_x + 6][pos_y] == spieler or \
            board[pos_x + 1][pos_y] == cpu and board[pos_x + 2][pos_y] == cpu and board[pos_x + 3][pos_y] == cpu and \
            board[pos_x + 4][pos_y] == cpu and board[pos_x + 5][pos_y] == cpu and board[pos_x + 6][pos_y] == cpu and \
            board[pos_x + 7][pos_y] == spieler:
            board[pos_x][pos_y] = spieler
            cpuSteineDrehen(board, pos_x, pos_y, cpu, spieler)
            drawBoard(board)
            spielstand(board)
        elif board[pos_x - 1][pos_y] == cpu and board[pos_x - 2][pos_y] == spieler or \
            board[pos_x - 1][pos_y] == cpu and board[pos_x - 2][pos_y] == cpu and board[pos_x - 3][pos_y] == spieler or \
            board[pos_x - 1][pos_y] == cpu and board[pos_x - 2][pos_y] == cpu and board[pos_x - 3][pos_y] == cpu and \
            board[pos_x - 4][pos_y] == spieler or \
            board[pos_x - 1][pos_y] == cpu and board[pos_x - 2][pos_y] == cpu and board[pos_x - 3][pos_y] == cpu and \
            board[pos_x - 4][pos_y] == cpu and board[pos_x - 5][pos_y] == spieler or \
            board[pos_x - 1][pos_y] == cpu and board[pos_x - 2][pos_y] == cpu and board[pos_x - 3][pos_y] == cpu and \
            board[pos_x - 4][pos_y] == cpu and board[pos_x - 5][pos_y] == cpu and board[pos_x - 6][pos_y] == spieler or \
            board[pos_x - 1][pos_y] == cpu and board[pos_x - 2][pos_y] == cpu and board[pos_x - 3][pos_y] == cpu and \
            board[pos_x - 4][pos_y] == cpu and board[pos_x - 5][pos_y] == cpu and board[pos_x - 6][pos_y] == cpu and \
            board[pos_x - 7][pos_y] == spieler:
            board[pos_x][pos_y] = spieler
            cpuSteineDrehen(board, pos_x, pos_y, cpu, spieler)
            drawBoard(board)
            spielstand(board)
        elif board[pos_x][pos_y + 1] == cpu and board[pos_x][pos_y + 2] == spieler or \
            board[pos_x][pos_y + 1] == cpu and board[pos_x][pos_y + 2] == cpu and board[pos_x][pos_y + 3] == spieler or \
            board[pos_x][pos_y + 1] == cpu and board[pos_x][pos_y + 2] == cpu and board[pos_x][pos_y + 3] == cpu and \
            board[pos_x][pos_y + 4] == spieler or \
            board[pos_x][pos_y + 1] == cpu and board[pos_x][pos_y + 2] == cpu and board[pos_x][pos_y + 3] == cpu and \
            board[pos_x][pos_y + 4] == cpu and board[pos_x][pos_y + 5] == spieler or \
            board[pos_x][pos_y + 1] == cpu and board[pos_x][pos_y + 2] == cpu and board[pos_x][pos_y + 3] == cpu and \
            board[pos_x][pos_y + 4] == cpu and board[pos_x][pos_y + 5] == cpu and board[pos_x][pos_y + 6] == spieler or \
            board[pos_x][pos_y + 1] == cpu and board[pos_x][pos_y + 2] == cpu and board[pos_x][pos_y + 3] == cpu and \
            board[pos_x][pos_y + 4] == cpu and board[pos_x][pos_y + 8] == cpu and board[pos_x][pos_y + 6] == cpu and \
            board[pos_x][pos_y + 7] == spieler:
            board[pos_x][pos_y] = spieler
            cpuSteineDrehen(board, pos_x, pos_y, cpu, spieler)
            drawBoard(board)
            spielstand(board)
        elif board[pos_x][pos_y - 1] == cpu and board[pos_x][pos_y - 2] == spieler or \
            board[pos_x][pos_y - 1] == cpu and board[pos_x][pos_y - 2] == cpu and board[pos_x][pos_y - 3] == spieler or \
            board[pos_x][pos_y - 1] == cpu and board[pos_x][pos_y - 2] == cpu and board[pos_x][pos_y - 3] == cpu and \
            board[pos_x][pos_y - 4] == spieler or \
            board[pos_x][pos_y - 1] == cpu and board[pos_x][pos_y - 2] == cpu and board[pos_x][pos_y - 3] == cpu and \
            board[pos_x][pos_y - 4] == cpu and board[pos_x][pos_y - 5] == spieler or \
            board[pos_x][pos_y - 1] == cpu and board[pos_x][pos_y - 2] == cpu and board[pos_x][pos_y - 3] == cpu and \
            board[pos_x][pos_y - 4] == cpu and board[pos_x][pos_y - 5] == cpu and board[pos_x][pos_y - 6] == spieler or \
            board[pos_x][pos_y - 1] == cpu and board[pos_x][pos_y - 2] == cpu and board[pos_x][pos_y - 3] == cpu and \
            board[pos_x][pos_y - 4] == cpu and board[pos_x][pos_y - 8] == cpu and board[pos_x][pos_y - 6] == cpu and \
            board[pos_x][pos_y - 7] == spieler:
            board[pos_x][pos_y] = spieler
            cpuSteineDrehen(board, pos_x, pos_y, cpu, spieler)
            drawBoard(board)
            spielstand(board)
        elif board[pos_x + 1][pos_y + 1] == cpu and board[pos_x + 2][pos_y + 2] == spieler or \
            board[pos_x + 1][pos_y + 1] == cpu and board[pos_x + 2][pos_y + 2] == cpu and board[pos_x + 3][pos_y + 3] == spieler or \
            board[pos_x + 1][pos_y + 1] == cpu and board[pos_x + 2][pos_y + 2] == cpu and board[pos_x + 3][pos_y + 3] == cpu and \
            board[pos_x + 4][pos_y + 4] == spieler or \
            board[pos_x + 1][pos_y + 1] == cpu and board[pos_x + 2][pos_y + 2] == cpu and board[pos_x + 3][pos_y + 3] == cpu and \
            board[pos_x + 4][pos_y + 4] == cpu and board[pos_x + 5][pos_y + 5] == spieler or \
            board[pos_x + 1][pos_y + 1] == cpu and board[pos_x + 2][pos_y + 2] == cpu and board[pos_x + 3][pos_y + 3] == cpu and \
            board[pos_x + 4][pos_y + 4] == cpu and board[pos_x + 5][pos_y + 5] == cpu and board[pos_x + 6][pos_y + 6] == spieler or \
            board[pos_x + 1][pos_y + 1] == cpu and board[pos_x + 2][pos_y + 2] == cpu and board[pos_x + 3][pos_y + 3] == cpu and \
            board[pos_x + 4][pos_y + 4] == cpu and board[pos_x + 5][pos_y + 5] == cpu and board[pos_x + 6][pos_y + 6] == cpu and \
            board[pos_x + 7][pos_y + 7] == spieler:
            board[pos_x][pos_y] = spieler
            cpuSteineDrehen(board, pos_x, pos_y, cpu, spieler)
            drawBoard(board)
            spielstand(board)
        elif board[pos_x - 1][pos_y - 1] == cpu and board[pos_x - 2][pos_y - 2] == spieler or \
            board[pos_x - 1][pos_y - 1] == cpu and board[pos_x - 2][pos_y - 2] == cpu and board[pos_x - 3][pos_y - 3] == spieler or \
            board[pos_x - 1][pos_y - 1] == cpu and board[pos_x - 2][pos_y - 2] == cpu and board[pos_x - 3][pos_y - 3] == cpu and \
            board[pos_x - 4][pos_y - 4] == spieler or \
            board[pos_x - 1][pos_y - 1] == cpu and board[pos_x - 2][pos_y - 2] == cpu and board[pos_x - 3][pos_y - 3] == cpu and \
            board[pos_x - 4][pos_y - 4] == cpu and board[pos_x - 5][pos_y- 5] == spieler or \
            board[pos_x - 1][pos_y - 1] == cpu and board[pos_x - 2][pos_y - 2] == cpu and board[pos_x - 3][pos_y - 3] == cpu and \
            board[pos_x - 4][pos_y - 4] == cpu and board[pos_x - 5][pos_y - 5] == cpu and board[pos_x - 6][pos_y - 6] == spieler or \
            board[pos_x - 1][pos_y - 1] == cpu and board[pos_x - 2][pos_y - 2] == cpu and board[pos_x - 3][pos_y - 3] == cpu and \
            board[pos_x - 4][pos_y - 4] == cpu and board[pos_x - 5][pos_y - 5] == cpu and board[pos_x - 6][pos_y - 6] == cpu and \
            board[pos_x - 7][pos_y - 7] == spieler:
            board[pos_x][pos_y] = spieler
            cpuSteineDrehen(board, pos_x, pos_y, cpu, spieler)
            drawBoard(board)
            spielstand(board)
        elif board[pos_x + 1][pos_y - 1] == cpu and board[pos_x + 2][pos_y - 2] == spieler or \
            board[pos_x + 1][pos_y - 1] == cpu and board[pos_x + 2][pos_y - 2] == cpu and board[pos_x + 3][pos_y - 3] == spieler or \
            board[pos_x + 1][pos_y - 1] == cpu and board[pos_x + 2][pos_y - 2] == cpu and board[pos_x + 3][pos_y - 3] == cpu and \
            board[pos_x + 4][pos_y - 4] == spieler or \
            board[pos_x + 1][pos_y - 1] == cpu and board[pos_x + 2][pos_y - 2] == cpu and board[pos_x + 3][pos_y - 3] == cpu and \
            board[pos_x + 4][pos_y - 4] == cpu and board[pos_x + 5][pos_y - 5] == spieler or \
            board[pos_x + 1][pos_y - 1] == cpu and board[pos_x + 2][pos_y - 2] == cpu and board[pos_x + 3][pos_y - 3] == cpu and \
            board[pos_x + 4][pos_y - 4] == cpu and board[pos_x + 5][pos_y - 5] == cpu and board[pos_x + 6][pos_y - 6] == spieler or \
            board[pos_x + 1][pos_y - 1] == cpu and board[pos_x + 2][pos_y - 2] == cpu and board[pos_x + 3][pos_y - 3] == cpu and \
            board[pos_x + 4][pos_y - 4] == cpu and board[pos_x + 5][pos_y - 5] == cpu and board[pos_x + 6][pos_y - 6] == cpu and \
            board[pos_x + 7][pos_y - 7] == spieler:
            board[pos_x][pos_y] = spieler
            cpuSteineDrehen(board, pos_x, pos_y, cpu, spieler)
            drawBoard(board)
            spielstand(board)
        elif board[pos_x - 1][pos_y + 1] == cpu and board[pos_x - 2][pos_y + 2] == spieler or \
            board[pos_x - 1][pos_y + 1] == cpu and board[pos_x - 2][pos_y + 2] == cpu and board[pos_x - 3][pos_y + 3] == spieler or \
            board[pos_x - 1][pos_y + 1] == cpu and board[pos_x - 2][pos_y + 2] == cpu and board[pos_x - 3][pos_y + 3] == cpu and \
            board[pos_x - 4][pos_y + 4] == spieler or \
            board[pos_x - 1][pos_y + 1] == cpu and board[pos_x - 2][pos_y + 2] == cpu and board[pos_x - 3][pos_y + 3] == cpu and \
            board[pos_x - 4][pos_y + 4] == cpu and board[pos_x - 5][pos_y + 5] == spieler or \
            board[pos_x - 1][pos_y + 1] == cpu and board[pos_x - 2][pos_y + 2] == cpu and board[pos_x - 3][pos_y + 3] == cpu and \
            board[pos_x - 4][pos_y + 4] == cpu and board[pos_x - 5][pos_y + 5] == cpu and board[pos_x - 6][pos_y + 6] == spieler or \
            board[pos_x - 1][pos_y + 1] == cpu and board[pos_x - 2][pos_y + 2] == cpu and board[pos_x - 3][pos_y + 3] == cpu and \
            board[pos_x - 4][pos_y + 4] == cpu and board[pos_x - 5][pos_y + 5] == cpu and board[pos_x - 6][pos_y + 6] == cpu and \
            board[pos_x - 7][pos_y + 7] == spieler:
            board[pos_x][pos_y] = spieler
            cpuSteineDrehen(board, pos_x, pos_y, cpu, spieler)
            drawBoard(board)
            spielstand(board)
            spielerZieht(board, start)
        else:
            print("Zug ist nicht möglich")
            spielerZieht(board,start)
        return board
    except:
        print("Zug ist nicht möglich")
        spielerZieht(board,start)

def cpuSteineDrehen(board, pos_x, pos_y, cpu, spieler):
    #print("hier werden die Steine der CPU umgedreht")
    print("Spielerzug:", (pos_x, pos_y))

    try:
        # überprüfe y[0] bis y[7]
        if cpu in board[pos_x][pos_y-1] and cpu in board[pos_x][pos_y-2] and cpu in board[pos_x][pos_y-3] and cpu in board[pos_x][pos_y-4] \
            and cpu in board[pos_x][pos_y-5] and cpu in board[pos_x][pos_y-6] \
            and spieler in board[pos_x][pos_y-7]:
            board[ pos_x ][ pos_y - 6 ] = spieler
            board[ pos_x ][ pos_y - 5 ] = spieler
            board[ pos_x ][ pos_y - 4 ] = spieler
            board[ pos_x ][ pos_y - 3 ] = spieler
            board[ pos_x ][ pos_y - 2 ] = spieler
            board[ pos_x ][ pos_y - 1 ] = spieler
            KI_Othello.R[pos_x][pos_y - 6] = -500
            KI_Othello.R[pos_x][pos_y - 5] = -500
            KI_Othello.R[pos_x][pos_y - 4] = -500
            KI_Othello.R[pos_x][pos_y - 3] = -500
            KI_Othello.R[pos_x][pos_y - 2] = -500
            KI_Othello.R[pos_x][pos_y - 1] = -500
        if cpu in board[pos_x][pos_y-1] and cpu in board[pos_x][pos_y-2] and cpu in board[pos_x][pos_y-3] and cpu in board[pos_x][pos_y-4] \
            and cpu in board[pos_x][pos_y-5]  \
            and spieler in board[pos_x][pos_y-6]:
            board[pos_x][pos_y-5] = spieler
            board[pos_x][pos_y-4] = spieler
            board[pos_x][pos_y-3] = spieler
            board[pos_x][pos_y-2] = spieler
            board[pos_x][pos_y-1] = spieler
            KI_Othello.R[pos_x][pos_y - 5] = -500
            KI_Othello.R[pos_x][pos_y - 4] = -500
            KI_Othello.R[pos_x][pos_y - 3] = -500
            KI_Othello.R[pos_x][pos_y - 2] = -500
            KI_Othello.R[pos_x][pos_y - 1] = -500
        elif cpu in board[pos_x][pos_y-1] and cpu in board[pos_x][pos_y-2] and cpu in board[pos_x][pos_y-3] and cpu in board[pos_x][pos_y-4] \
            and spieler in board[pos_x][pos_y-5]:
            board[pos_x][pos_y-4] = spieler
            board[pos_x][pos_y-3] = spieler
            board[pos_x][pos_y-2] = spieler
            board[pos_x][pos_y-1] = spieler
            KI_Othello.R[pos_x][pos_y - 4] = -500
            KI_Othello.R[pos_x][pos_y - 3] = -500
            KI_Othello.R[pos_x][pos_y - 2] = -500
            KI_Othello.R[pos_x][pos_y - 1] = -500
        elif cpu in board[pos_x][pos_y-1] and cpu in board[pos_x][pos_y-2] and cpu in board[pos_x][pos_y-3] \
            and spieler in board[pos_x][pos_y-4]:
            board[pos_x][pos_y-3] = spieler
            board[pos_x][pos_y-2] = spieler
            board[pos_x][pos_y-1] = spieler
            KI_Othello.R[pos_x][pos_y - 3] = -500
            KI_Othello.R[pos_x][pos_y - 2] = -500
            KI_Othello.R[pos_x][pos_y - 1] = -500
        elif cpu in board[pos_x][pos_y-1] and cpu in board[pos_x][pos_y-2] \
            and spieler in board[pos_x][pos_y-3]:
            board[pos_x][pos_y-2] = spieler
            board[pos_x][pos_y-1] = spieler
            KI_Othello.R[pos_x][pos_y - 2] = -500
            KI_Othello.R[pos_x][pos_y - 1] = -500
        elif cpu in board[pos_x][pos_y-1] \
            and spieler in board[pos_x][pos_y-2]:
            board[pos_x][pos_y-1] = spieler
            KI_Othello.R[pos_x][pos_y - 1] = -500

        # überprüfe y[7] bis y[0]
        if cpu in board[pos_x][pos_y+1] and cpu in board[pos_x][pos_y+2] and cpu in board[pos_x][pos_y+3] and cpu in board[pos_x][pos_y+4] \
            and cpu in board[pos_x][pos_y+5] and cpu in board[pos_x][pos_y+6] \
            and spieler in board[pos_x][pos_y+7]:
            board[pos_x][pos_y+6] = spieler
            board[pos_x][pos_y+5] = spieler
            board[pos_x][pos_y+4] = spieler
            board[pos_x][pos_y+3] = spieler
            board[pos_x][pos_y+2] = spieler
            board[pos_x][pos_y+1] = spieler
            KI_Othello.R[pos_x][pos_y + 6] = -500
            KI_Othello.R[pos_x][pos_y + 5] = -500
            KI_Othello.R[pos_x][pos_y + 4] = -500
            KI_Othello.R[pos_x][pos_y + 3] = -500
            KI_Othello.R[pos_x][pos_y + 2] = -500
            KI_Othello.R[pos_x][pos_y + 1] = -500
        elif cpu in board[pos_x][pos_y+1] and cpu in board[pos_x][pos_y+2] and cpu in board[pos_x][pos_y+3] and cpu in board[pos_x][pos_y+4] \
            and cpu in board[pos_x][pos_y+5]  \
            and spieler in board[pos_x][pos_y+6]:
            board[pos_x][pos_y+5] = spieler
            board[pos_x][pos_y+4] = spieler
            board[pos_x][pos_y+3] = spieler
            board[pos_x][pos_y+2] = spieler
            board[pos_x][pos_y+1] = spieler
            KI_Othello.R[pos_x][pos_y + 5] = -500
            KI_Othello.R[pos_x][pos_y + 4] = -500
            KI_Othello.R[pos_x][pos_y + 3] = -500
            KI_Othello.R[pos_x][pos_y + 2] = -500
            KI_Othello.R[pos_x][pos_y + 1] = -500
        elif cpu in board[pos_x][pos_y+1] and cpu in board[pos_x][pos_y+2] and cpu in board[pos_x][pos_y+3] and cpu in board[pos_x][pos_y+4] \
            and spieler in board[pos_x][pos_y+5]:
            board[pos_x][pos_y+4] = spieler
            board[pos_x][pos_y+3] = spieler
            board[pos_x][pos_y+2] = spieler
            board[pos_x][pos_y+1] = spieler
            KI_Othello.R[pos_x][pos_y + 4] = -500
            KI_Othello.R[pos_x][pos_y + 3] = -500
            KI_Othello.R[pos_x][pos_y + 2] = -500
            KI_Othello.R[pos_x][pos_y + 1] = -500
        elif cpu in board[pos_x][pos_y+1] and cpu in board[pos_x][pos_y+2] and cpu in board[pos_x][pos_y+3] \
            and spieler in board[pos_x][pos_y+4]:
            board[pos_x][pos_y+3] = spieler
            board[pos_x][pos_y+2] = spieler
            board[pos_x][pos_y+1] = spieler
            KI_Othello.R[pos_x][pos_y + 3] = -500
            KI_Othello.R[pos_x][pos_y + 2] = -500
            KI_Othello.R[pos_x][pos_y + 1] = -500
        elif cpu in board[pos_x][pos_y+1] and cpu in board[pos_x][pos_y+2] \
            and spieler in board[pos_x][pos_y+3]:
            board[pos_x][pos_y+2] = spieler
            board[pos_x][pos_y+1] = spieler
            KI_Othello.R[pos_x][pos_y + 2] = -500
            KI_Othello.R[pos_x][pos_y + 1] = -500
        elif cpu in board[pos_x][pos_y+1] \
            and spieler in board[pos_x][pos_y+2]:
            board[pos_x][pos_y+1] = spieler
            KI_Othello.R[pos_x][pos_y + 1] = -500

        # überprüfe x[0] bis x[7]
        if cpu in board[pos_x+1][pos_y] and cpu in board[pos_x+2][pos_y] and cpu in board[pos_x+3][pos_y] and cpu in board[pos_x+4][pos_y] \
            and cpu in board[pos_x+5][pos_y] and cpu in board[pos_x+6][pos_y] \
            and spieler in board[pos_x+7][pos_y]:
            board[pos_x+6][pos_y] = spieler
            board[pos_x+5][pos_y] = spieler
            board[pos_x+4][pos_y] = spieler
            board[pos_x+3][pos_y] = spieler
            board[pos_x+2][pos_y] = spieler
            board[pos_x+1][pos_y] = spieler
            KI_Othello.R[pos_x + 6][pos_y] = -500
            KI_Othello.R[pos_x + 5][pos_y] = -500
            KI_Othello.R[pos_x + 4][pos_y] = -500
            KI_Othello.R[pos_x + 3][pos_y] = -500
            KI_Othello.R[pos_x + 2][pos_y] = -500
            KI_Othello.R[pos_x + 1][pos_y] = -500
        elif cpu in board[pos_x+1][pos_y] and cpu in board[pos_x+2][pos_y] and cpu in board[pos_x+3][pos_y] and cpu in board[pos_x+4][pos_y] \
            and cpu in board[pos_x+5][pos_y]  \
            and spieler in board[pos_x][pos_y]:
            board[pos_x+5][pos_y] = spieler
            board[pos_x+4][pos_y] = spieler
            board[pos_x+3][pos_y] = spieler
            board[pos_x+2][pos_y] = spieler
            board[pos_x+1][pos_y] = spieler
            KI_Othello.R[pos_x + 5][pos_y] = -500
            KI_Othello.R[pos_x + 4][pos_y] = -500
            KI_Othello.R[pos_x + 3][pos_y] = -500
            KI_Othello.R[pos_x + 2][pos_y] = -500
            KI_Othello.R[pos_x + 1][pos_y] = -500
        elif cpu in board[pos_x+1][pos_y] and cpu in board[pos_x+2][pos_y] and cpu in board[pos_x+3][pos_y] and cpu in board[pos_x+4][pos_y] \
            and spieler in board[pos_x+5][pos_y]:
            board[pos_x+4][pos_y] = spieler
            board[pos_x+3][pos_y] = spieler
            board[pos_x+2][pos_y] = spieler
            board[pos_x+1][pos_y] = spieler
            KI_Othello.R[pos_x + 4][pos_y] = -500
            KI_Othello.R[pos_x + 3][pos_y] = -500
            KI_Othello.R[pos_x + 2][pos_y] = -500
            KI_Othello.R[pos_x + 1][pos_y] = -500
        elif cpu in board[pos_x+1][pos_y] and cpu in board[pos_x+2][pos_y] and cpu in board[pos_x+3][pos_y] \
            and spieler in board[pos_x+4][pos_y]:
            board[pos_x+3][pos_y] = spieler
            board[pos_x+2][pos_y] = spieler
            board[pos_x+1][pos_y] = spieler
            KI_Othello.R[pos_x + 3][pos_y] = -500
            KI_Othello.R[pos_x + 2][pos_y] = -500
            KI_Othello.R[pos_x + 1][pos_y] = -500
        elif cpu in board[pos_x+1][pos_y] and cpu in board[pos_x+2][pos_y] \
            and spieler in board[pos_x+3][pos_y]:
            board[pos_x+2][pos_y] = spieler
            board[pos_x+1][pos_y] = spieler
            KI_Othello.R[pos_x + 2][pos_y] = -500
            KI_Othello.R[pos_x + 1][pos_y] = -500
        elif cpu in board[pos_x+1][pos_y] \
            and spieler in board[pos_x+2][pos_y]:
            board[pos_x+1][pos_y] = spieler
            KI_Othello.R[pos_x + 1][pos_y] = -500

        # überprüfe x[7] bis x[0]
        if cpu in board[pos_x-1][pos_y] and cpu in board[pos_x-2][pos_y] and cpu in board[pos_x-3][pos_y] and cpu in board[pos_x-4][pos_y] \
            and cpu in board[pos_x-5][pos_y] and cpu in board[pos_x-6][pos_y] \
            and spieler in board[pos_x-7][pos_y]:
            board[pos_x-6][pos_y] = spieler
            board[pos_x-5][pos_y] = spieler
            board[pos_x-4][pos_y] = spieler
            board[pos_x-3][pos_y] = spieler
            board[pos_x-2][pos_y] = spieler
            board[pos_x-1][pos_y] = spieler
            KI_Othello.R[pos_x - 6][pos_y] = -500
            KI_Othello.R[pos_x - 5][pos_y] = -500
            KI_Othello.R[pos_x - 4][pos_y] = -500
            KI_Othello.R[pos_x - 3][pos_y] = -500
            KI_Othello.R[pos_x - 2][pos_y] = -500
            KI_Othello.R[pos_x - 1][pos_y] = -500
        elif cpu in board[pos_x-1][pos_y] and cpu in board[pos_x-2][pos_y] and cpu in board[pos_x-3][pos_y] and cpu in board[pos_x-4][pos_y] \
            and cpu in board[pos_x-5][pos_y]  \
            and spieler in board[pos_x][pos_y]:
            board[pos_x-5][pos_y] = spieler
            board[pos_x-4][pos_y] = spieler
            board[pos_x-3][pos_y] = spieler
            board[pos_x-2][pos_y] = spieler
            board[pos_x-1][pos_y] = spieler
            KI_Othello.R[pos_x - 5][pos_y] = -500
            KI_Othello.R[pos_x - 4][pos_y] = -500
            KI_Othello.R[pos_x - 3][pos_y] = -500
            KI_Othello.R[pos_x - 2][pos_y] = -500
            KI_Othello.R[pos_x - 1][pos_y] = -500
        elif cpu in board[pos_x-1][pos_y] and cpu in board[pos_x-2][pos_y] and cpu in board[pos_x-3][pos_y] and cpu in board[pos_x-4][pos_y] \
            and spieler in board[pos_x-5][pos_y]:
            board[pos_x-4][pos_y] = spieler
            board[pos_x-3][pos_y] = spieler
            board[pos_x-2][pos_y] = spieler
            board[pos_x-1][pos_y] = spieler
            KI_Othello.R[pos_x - 4][pos_y] = -500
            KI_Othello.R[pos_x - 3][pos_y] = -500
            KI_Othello.R[pos_x - 2][pos_y] = -500
            KI_Othello.R[pos_x - 1][pos_y] = -500
        elif cpu in board[pos_x-1][pos_y] and cpu in board[pos_x-2][pos_y] and cpu in board[pos_x-3][pos_y] \
            and spieler in board[pos_x-4][pos_y]:
            board[pos_x-3][pos_y] = spieler
            board[pos_x-2][pos_y] = spieler
            board[pos_x-1][pos_y] = spieler
            KI_Othello.R[pos_x - 3][pos_y] = -500
            KI_Othello.R[pos_x - 2][pos_y] = -500
            KI_Othello.R[pos_x - 1][pos_y] = -500
        elif cpu in board[pos_x-1][pos_y] and cpu in board[pos_x-2][pos_y] \
            and spieler in board[pos_x-3][pos_y]:
            board[pos_x-2][pos_y] = spieler
            board[pos_x-1][pos_y] = spieler
            KI_Othello.R[pos_x - 2][pos_y] = -500
            KI_Othello.R[pos_x - 1][pos_y] = -500
        elif cpu in board[pos_x-1][pos_y] \
            and spieler in board[pos_x-2][pos_y]:
            board[pos_x-1][pos_y] = spieler
            KI_Othello.R[pos_x - 1][pos_y] = -500

        # überprüfe x+ y-
        if cpu in board[pos_x+1][pos_y-1] and cpu in board[pos_x+2][pos_y-2] and cpu in board[pos_x+3][pos_y-3] and cpu in board[pos_x+4][pos_y-4] \
            and cpu in board[pos_x+5][pos_y-5] and cpu in board[pos_x+6][pos_y-6] \
            and spieler in board[pos_x+7][pos_y]:
            board[pos_x+6][pos_y-6] = spieler
            board[pos_x+5][pos_y-5] = spieler
            board[pos_x+4][pos_y-4] = spieler
            board[pos_x+3][pos_y-3] = spieler
            board[pos_x+2][pos_y-2] = spieler
            board[pos_x+1][pos_y-1] = spieler
            KI_Othello.R[pos_x + 6][pos_y - 6] = -500
            KI_Othello.R[pos_x + 5][pos_y - 5] = -500
            KI_Othello.R[pos_x + 4][pos_y - 4] = -500
            KI_Othello.R[pos_x + 3][pos_y - 3] = -500
            KI_Othello.R[pos_x + 2][pos_y - 2] = -500
            KI_Othello.R[pos_x + 1][pos_y - 1] = -500
        elif cpu in board[pos_x+1][pos_y-1] and cpu in board[pos_x+2][pos_y-2] and cpu in board[pos_x+3][pos_y-3] and cpu in board[pos_x+4][pos_y-4] \
            and cpu in board[pos_x+5][pos_y-5]  \
            and spieler in board[pos_x][pos_y]:
            board[pos_x+5][pos_y-5] = spieler
            board[pos_x+4][pos_y-4] = spieler
            board[pos_x+3][pos_y-3] = spieler
            board[pos_x+2][pos_y-2] = spieler
            board[pos_x+1][pos_y-1] = spieler
            KI_Othello.R[pos_x + 5][pos_y - 5] = -500
            KI_Othello.R[pos_x + 4][pos_y - 4] = -500
            KI_Othello.R[pos_x + 3][pos_y - 3] = -500
            KI_Othello.R[pos_x + 2][pos_y - 2] = -500
            KI_Othello.R[pos_x + 1][pos_y - 1] = -500
        elif cpu in board[pos_x+1][pos_y-1] and cpu in board[pos_x+2][pos_y-2] and cpu in board[pos_x+3][pos_y-3] and cpu in board[pos_x+4][pos_y-4] \
            and spieler in board[pos_x+5][pos_y-5]:
            board[pos_x+4][pos_y-4] = spieler
            board[pos_x+3][pos_y-3] = spieler
            board[pos_x+2][pos_y-2] = spieler
            board[pos_x+1][pos_y-1] = spieler
            KI_Othello.R[pos_x + 4][pos_y - 4] = -500
            KI_Othello.R[pos_x + 3][pos_y - 3] = -500
            KI_Othello.R[pos_x + 2][pos_y - 2] = -500
            KI_Othello.R[pos_x + 1][pos_y - 1] = -500
        elif cpu in board[pos_x+1][pos_y-1] and cpu in board[pos_x+2][pos_y-2] and cpu in board[pos_x+3][pos_y-3] \
            and spieler in board[pos_x+4][pos_y-4]:
            board[pos_x+3][pos_y-3] = spieler
            board[pos_x+2][pos_y-2] = spieler
            board[pos_x+1][pos_y-1] = spieler
            KI_Othello.R[pos_x + 3][pos_y - 3] = -500
            KI_Othello.R[pos_x + 2][pos_y - 2] = -500
            KI_Othello.R[pos_x + 1][pos_y - 1] = -500
        elif cpu in board[pos_x+1][pos_y-1] and cpu in board[pos_x+2][pos_y-2] \
            and spieler in board[pos_x+3][pos_y-3]:
            board[pos_x+2][pos_y-2] = spieler
            board[pos_x+1][pos_y-1] = spieler
            KI_Othello.R[pos_x + 2][pos_y - 2] = -500
            KI_Othello.R[pos_x + 1][pos_y - 1] = -500
        elif cpu in board[pos_x+1][pos_y-1] \
            and spieler in board[pos_x+2][pos_y-2]:
            board[pos_x+1][pos_y-1] = spieler
            KI_Othello.R[pos_x + 1][pos_y - 1] = -500

        # überprüfe 7,0 bis 0,7
        if cpu in board[pos_x-1][pos_y+1] and cpu in board[pos_x-2][pos_y+2] and cpu in board[pos_x-3][pos_y+3] and cpu in board[pos_x-4][pos_y+4] \
            and cpu in board[pos_x-5][pos_y+5] and cpu in board[pos_x-6][pos_y+6] \
            and spieler in board[pos_x-7][pos_y]:
            board[pos_x-6][pos_y+6] = spieler
            board[pos_x-5][pos_y+5] = spieler
            board[pos_x-4][pos_y+4] = spieler
            board[pos_x-3][pos_y+3] = spieler
            board[pos_x-2][pos_y+2] = spieler
            board[pos_x-1][pos_y+1] = spieler
            KI_Othello.R[pos_x - 6][pos_y + 6] = -500
            KI_Othello.R[pos_x - 5][pos_y + 5] = -500
            KI_Othello.R[pos_x - 4][pos_y + 4] = -500
            KI_Othello.R[pos_x - 3][pos_y + 3] = -500
            KI_Othello.R[pos_x - 2][pos_y + 2] = -500
            KI_Othello.R[pos_x - 1][pos_y + 1] = -500
        elif cpu in board[pos_x-1][pos_y+1] and cpu in board[pos_x-2][pos_y+2] and cpu in board[pos_x-3][pos_y+3] and cpu in board[pos_x-4][pos_y+4] \
            and cpu in board[pos_x-5][pos_y+5]  \
            and spieler in board[pos_x][pos_y]:
            board[pos_x-5][pos_y+5] = spieler
            board[pos_x-4][pos_y+4] = spieler
            board[pos_x-3][pos_y+3] = spieler
            board[pos_x-2][pos_y+2] = spieler
            board[pos_x-1][pos_y+1] = spieler
            KI_Othello.R[pos_x - 5][pos_y + 5] = -500
            KI_Othello.R[pos_x - 4][pos_y + 4] = -500
            KI_Othello.R[pos_x - 3][pos_y + 3] = -500
            KI_Othello.R[pos_x - 2][pos_y + 2] = -500
            KI_Othello.R[pos_x - 1][pos_y + 1] = -500
        elif cpu in board[pos_x-1][pos_y+1] and cpu in board[pos_x-2][pos_y+2] and cpu in board[pos_x-3][pos_y+3] and cpu in board[pos_x-4][pos_y+4] \
            and spieler in board[pos_x-5][pos_y+5]:
            board[pos_x-4][pos_y+4] = spieler
            board[pos_x-3][pos_y+3] = spieler
            board[pos_x-2][pos_y+2] = spieler
            board[pos_x-1][pos_y+1] = spieler
            KI_Othello.R[pos_x - 4][pos_y + 4] = -500
            KI_Othello.R[pos_x - 3][pos_y + 3] = -500
            KI_Othello.R[pos_x - 2][pos_y + 2] = -500
            KI_Othello.R[pos_x - 1][pos_y + 1] = -500
        elif cpu in board[pos_x-1][pos_y+1] and cpu in board[pos_x-2][pos_y+2] and cpu in board[pos_x-3][pos_y+3] \
            and spieler in board[pos_x-4][pos_y+4]:
            board[pos_x-3][pos_y+3] = spieler
            board[pos_x-2][pos_y+2] = spieler
            board[pos_x-1][pos_y+1] = spieler
            KI_Othello.R[pos_x - 3][pos_y + 3] = -500
            KI_Othello.R[pos_x - 2][pos_y + 2] = -500
            KI_Othello.R[pos_x - 1][pos_y + 1] = -500
        elif cpu in board[pos_x-1][pos_y+1] and cpu in board[pos_x-2][pos_y+2] \
            and spieler in board[pos_x-3][pos_y+3]:
            board[pos_x-2][pos_y+2] = spieler
            board[pos_x-1][pos_y+1] = spieler
            KI_Othello.R[pos_x - 2][pos_y + 2] = -500
            KI_Othello.R[pos_x - 1][pos_y + 1] = -500
        elif cpu in board[pos_x-1][pos_y+1] \
            and spieler in board[pos_x-2][pos_y+2]:
            board[pos_x-1][pos_y+1] = spieler
            KI_Othello.R[pos_x - 1][pos_y + 1] = -500

        # überprüfe 7,0 bis 0,0
        if cpu in board[pos_x - 1][pos_y - 1] and cpu in board[pos_x - 2][pos_y - 2] and cpu in board[pos_x - 3][
            pos_y - 3] and cpu in board[pos_x - 4][pos_y - 4] \
                and cpu in board[pos_x - 5][pos_y - 5] and cpu in board[pos_x - 6][pos_y - 6] \
                and spieler in board[pos_x - 7][pos_y]:
            board[pos_x - 6][pos_y - 6] = spieler
            board[pos_x - 5][pos_y - 5] = spieler
            board[pos_x - 4][pos_y - 4] = spieler
            board[pos_x - 3][pos_y - 3] = spieler
            board[pos_x - 2][pos_y - 2] = spieler
            board[pos_x - 1][pos_y - 1] = spieler
            KI_Othello.R[pos_x - 6][pos_y - 6] = -500
            KI_Othello.R[pos_x - 5][pos_y - 5] = -500
            KI_Othello.R[pos_x - 4][pos_y - 4] = -500
            KI_Othello.R[pos_x - 3][pos_y - 3] = -500
            KI_Othello.R[pos_x - 2][pos_y - 2] = -500
            KI_Othello.R[pos_x - 1][pos_y - 1] = -500
        elif cpu in board[pos_x - 1][pos_y - 1] and cpu in board[pos_x - 2][pos_y - 2] and cpu in board[pos_x - 3][
            pos_y - 3] and cpu in board[pos_x - 4][pos_y - 4] \
                and cpu in board[pos_x - 5][pos_y - 5] \
                and spieler in board[pos_x][pos_y]:
            board[pos_x - 5][pos_y - 5] = spieler
            board[pos_x - 4][pos_y - 4] = spieler
            board[pos_x - 3][pos_y - 3] = spieler
            board[pos_x - 2][pos_y - 2] = spieler
            board[pos_x - 1][pos_y - 1] = spieler
            KI_Othello.R[pos_x - 5][pos_y - 5] = -500
            KI_Othello.R[pos_x - 4][pos_y - 4] = -500
            KI_Othello.R[pos_x - 3][pos_y - 3] = -500
            KI_Othello.R[pos_x - 2][pos_y - 2] = -500
            KI_Othello.R[pos_x - 1][pos_y - 1] = -500
        elif cpu in board[pos_x - 1][pos_y - 1] and cpu in board[pos_x - 2][pos_y - 2] and cpu in board[pos_x - 3][
            pos_y - 3] and cpu in board[pos_x - 4][pos_y - 4] \
                and spieler in board[pos_x - 5][pos_y - 5]:
            board[pos_x - 4][pos_y - 4] = spieler
            board[pos_x - 3][pos_y - 3] = spieler
            board[pos_x - 2][pos_y - 2] = spieler
            board[pos_x - 1][pos_y - 1] = spieler
            KI_Othello.R[pos_x - 4][pos_y - 4] = -500
            KI_Othello.R[pos_x - 3][pos_y - 3] = -500
            KI_Othello.R[pos_x - 2][pos_y - 2] = -500
            KI_Othello.R[pos_x - 1][pos_y - 1] = -500
        elif cpu in board[pos_x - 1][pos_y - 1] and cpu in board[pos_x - 2][pos_y - 2] and cpu in board[pos_x - 3][
            pos_y - 3] \
                and spieler in board[pos_x - 4][pos_y - 4]:
            board[pos_x - 3][pos_y - 3] = spieler
            board[pos_x - 2][pos_y - 2] = spieler
            board[pos_x - 1][pos_y - 1] = spieler
            KI_Othello.R[pos_x - 3][pos_y - 3] = -500
            KI_Othello.R[pos_x - 2][pos_y - 2] = -500
            KI_Othello.R[pos_x - 1][pos_y - 1] = -500
        elif cpu in board[pos_x - 1][pos_y - 1] and cpu in board[pos_x - 2][pos_y - 2] \
                and spieler in board[pos_x - 3][pos_y - 3]:
            board[pos_x - 2][pos_y - 2] = spieler
            board[pos_x - 1][pos_y - 1] = spieler
            KI_Othello.R[pos_x - 2][pos_y - 2] = -500
            KI_Othello.R[pos_x - 1][pos_y - 1] = -500
        elif cpu in board[pos_x - 1][pos_y - 1] \
                and spieler in board[pos_x - 2][pos_y - 2]:
            board[pos_x - 1][pos_y - 1] = spieler
            KI_Othello.R[pos_x - 1][pos_y - 1] = -500

        # überprüfe x+ y+
        if cpu in board[pos_x + 1][pos_y + 1] and cpu in board[pos_x + 2][pos_y + 2] and cpu in board[pos_x + 3][
            pos_y + 3] and cpu in board[pos_x + 4][pos_y + 4] \
                and cpu in board[pos_x + 5][pos_y + 5] and cpu in board[pos_x + 6][pos_y + 6] \
                and spieler in board[pos_x + 7][pos_y]:
            board[pos_x + 6][pos_y + 6] = spieler
            board[pos_x + 5][pos_y + 5] = spieler
            board[pos_x + 4][pos_y + 4] = spieler
            board[pos_x + 3][pos_y + 3] = spieler
            board[pos_x + 2][pos_y + 2] = spieler
            board[pos_x + 1][pos_y + 1] = spieler
            KI_Othello.R[pos_x + 6][pos_y + 6] = -500
            KI_Othello.R[pos_x + 5][pos_y + 5] = -500
            KI_Othello.R[pos_x + 4][pos_y + 4] = -500
            KI_Othello.R[pos_x + 3][pos_y + 3] = -500
            KI_Othello.R[pos_x + 2][pos_y + 2] = -500
            KI_Othello.R[pos_x + 1][pos_y + 1] = -500
        elif cpu in board[pos_x + 1][pos_y + 1] and cpu in board[pos_x + 2][pos_y + 2] and cpu in board[pos_x + 3][
            pos_y + 3] and cpu in board[pos_x + 4][pos_y + 4] \
                and cpu in board[pos_x + 5][pos_y + 5] \
                and spieler in board[pos_x][pos_y]:
            board[pos_x + 5][pos_y + 5] = spieler
            board[pos_x + 4][pos_y + 4] = spieler
            board[pos_x + 3][pos_y + 3] = spieler
            board[pos_x + 2][pos_y + 2] = spieler
            board[pos_x + 1][pos_y + 1] = spieler
            KI_Othello.R[pos_x + 5][pos_y + 5] = -500
            KI_Othello.R[pos_x + 4][pos_y + 4] = -500
            KI_Othello.R[pos_x + 3][pos_y + 3] = -500
            KI_Othello.R[pos_x + 2][pos_y + 2] = -500
            KI_Othello.R[pos_x + 1][pos_y + 1] = -500
        elif cpu in board[pos_x + 1][pos_y + 1] and cpu in board[pos_x + 2][pos_y + 2] and cpu in board[pos_x + 3][
            pos_y + 3] and cpu in board[pos_x + 4][pos_y + 4] \
                and spieler in board[pos_x + 5][pos_y + 5]:
            board[pos_x + 4][pos_y + 4] = spieler
            board[pos_x + 3][pos_y + 3] = spieler
            board[pos_x + 2][pos_y + 2] = spieler
            board[pos_x + 1][pos_y + 1] = spieler
            KI_Othello.R[pos_x + 4][pos_y + 4] = -500
            KI_Othello.R[pos_x + 3][pos_y + 3] = -500
            KI_Othello.R[pos_x + 2][pos_y + 2] = -500
            KI_Othello.R[pos_x + 1][pos_y + 1] = -500
        elif cpu in board[pos_x + 1][pos_y + 1] and cpu in board[pos_x + 2][pos_y + 2] and cpu in board[pos_x + 3][
            pos_y + 3] \
                and spieler in board[pos_x + 4][pos_y + 4]:

            board[pos_x + 3][pos_y + 3] = spieler
            board[pos_x + 2][pos_y + 2] = spieler
            board[pos_x + 1][pos_y + 1] = spieler
            KI_Othello.R[pos_x + 3][pos_y + 3] = -500
            KI_Othello.R[pos_x + 2][pos_y + 2] = -500
            KI_Othello.R[pos_x + 1][pos_y + 1] = -500
        elif cpu in board[pos_x + 1][pos_y + 1] and cpu in board[pos_x + 2][pos_y + 2] \
                and spieler in board[pos_x + 3][pos_y + 3]:
            board[pos_x + 2][pos_y + 2] = spieler
            board[pos_x + 1][pos_y + 1] = spieler
            KI_Othello.R[pos_x + 2][pos_y + 2] = -500
            KI_Othello.R[pos_x + 1][pos_y + 1] = -500
        elif cpu in board[pos_x + 1][pos_y + 1] \
                and spieler in board[pos_x + 2][pos_y + 2]:
            board[pos_x + 1][pos_y + 1] = spieler
            KI_Othello.R[pos_x + 1][pos_y + 1] = -500
    except:
        print("Zug ist nicht möglich")
        spielerZieht(board, start)

    print()

def spielerSteineDrehen(board, pos_x, pos_y, cpu, spieler):
    #print("hier werden die Steine des Spielers umgedreht")
    print("KI-Zug:", (pos_x, pos_y))

    try:
        # überprüfe y[0] bis y[7]
        if spieler in board[pos_x][pos_y - 1] and spieler in board[pos_x][pos_y - 2] and spieler in board[pos_x][
            pos_y - 3] and spieler in board[pos_x][pos_y - 4] \
                and spieler in board[pos_x][pos_y - 5] and spieler in board[pos_x][pos_y - 6] \
                and cpu in board[pos_x][pos_y - 7]:
            board[pos_x][pos_y - 6] = cpu
            board[pos_x][pos_y - 5] = cpu
            board[pos_x][pos_y - 4] = cpu
            board[pos_x][pos_y - 3] = cpu
            board[pos_x][pos_y - 2] = cpu
            board[pos_x][pos_y - 1] = cpu
            KI_Othello.R[pos_x][pos_y - 6] = -500
            KI_Othello.R[pos_x][pos_y - 5] = -500
            KI_Othello.R[pos_x][pos_y - 4] = -500
            KI_Othello.R[pos_x][pos_y - 3] = -500
            KI_Othello.R[pos_x][pos_y - 2] = -500
            KI_Othello.R[pos_x][pos_y - 1] = -500
        if spieler in board[pos_x][pos_y - 1] and spieler in board[pos_x][pos_y - 2] and spieler in board[pos_x][
            pos_y - 3] and spieler in board[pos_x][pos_y - 4] \
                and spieler in board[pos_x][pos_y - 5] \
                and cpu in board[pos_x][pos_y - 6]:
            board[pos_x][pos_y - 5] = cpu
            board[pos_x][pos_y - 4] = cpu
            board[pos_x][pos_y - 3] = cpu
            board[pos_x][pos_y - 2] = cpu
            board[pos_x][pos_y - 1] = cpu
            KI_Othello.R[pos_x][pos_y - 5] = -500
            KI_Othello.R[pos_x][pos_y - 4] = -500
            KI_Othello.R[pos_x][pos_y - 3] = -500
            KI_Othello.R[pos_x][pos_y - 2] = -500
            KI_Othello.R[pos_x][pos_y - 1] = -500
        elif spieler in board[pos_x][pos_y - 1] and spieler in board[pos_x][pos_y - 2] and spieler in board[pos_x][
            pos_y - 3] and spieler in board[pos_x][pos_y - 4] \
                and cpu in board[pos_x][pos_y - 5]:
            board[pos_x][pos_y - 4] = cpu
            board[pos_x][pos_y - 3] = cpu
            board[pos_x][pos_y - 2] = cpu
            board[pos_x][pos_y - 1] = cpu
            KI_Othello.R[pos_x][pos_y - 4] = -500
            KI_Othello.R[pos_x][pos_y - 3] = -500
            KI_Othello.R[pos_x][pos_y - 2] = -500
            KI_Othello.R[pos_x][pos_y - 1] = -500
        elif spieler in board[pos_x][pos_y - 1] and spieler in board[pos_x][pos_y - 2] and spieler in board[pos_x][pos_y - 3] \
                and cpu in board[pos_x][pos_y - 4]:
            board[pos_x][pos_y - 3] = cpu
            board[pos_x][pos_y - 2] = cpu
            board[pos_x][pos_y - 1] = cpu
            KI_Othello.R[pos_x][pos_y - 3] = -500
            KI_Othello.R[pos_x][pos_y - 2] = -500
            KI_Othello.R[pos_x][pos_y - 1] = -500
        elif spieler in board[pos_x][pos_y - 1] and spieler in board[pos_x][pos_y - 2] \
                and cpu in board[pos_x][pos_y - 3]:
            board[pos_x][pos_y - 2] = cpu
            board[pos_x][pos_y - 1] = cpu
            KI_Othello.R[pos_x][pos_y - 2] = -500
            KI_Othello.R[pos_x][pos_y - 1] = -500
        elif spieler in board[pos_x][pos_y - 1] \
                and cpu in board[pos_x][pos_y - 2]:
            board[pos_x][pos_y - 1] = cpu
            KI_Othello.R[pos_x][pos_y - 1] = -500

        # überprüfe y[7] bis y[0]
        if spieler in board[pos_x][pos_y + 1] and spieler in board[pos_x][pos_y + 2] and spieler in board[pos_x][
            pos_y + 3] and spieler in board[pos_x][pos_y + 4] \
                and spieler in board[pos_x][pos_y + 5] and spieler in board[pos_x][pos_y + 6] \
                and cpu in board[pos_x][pos_y + 7]:
            board[pos_x][pos_y + 6] = cpu
            board[pos_x][pos_y + 5] = cpu
            board[pos_x][pos_y + 4] = cpu
            board[pos_x][pos_y + 3] = cpu
            board[pos_x][pos_y + 2] = cpu
            board[pos_x][pos_y + 1] = cpu
            KI_Othello.R[pos_x][pos_y + 6] = -500
            KI_Othello.R[pos_x][pos_y + 5] = -500
            KI_Othello.R[pos_x][pos_y + 4] = -500
            KI_Othello.R[pos_x][pos_y + 3] = -500
            KI_Othello.R[pos_x][pos_y + 2] = -500
            KI_Othello.R[pos_x][pos_y + 1] = -500
        elif spieler in board[pos_x][pos_y + 1] and spieler in board[pos_x][pos_y + 2] and spieler in board[pos_x][
            pos_y + 3] and spieler in board[pos_x][pos_y + 4] \
                and spieler in board[pos_x][pos_y + 5] \
                and cpu in board[pos_x][pos_y + 6]:
            board[pos_x][pos_y + 5] = cpu
            board[pos_x][pos_y + 4] = cpu
            board[pos_x][pos_y + 3] = cpu
            board[pos_x][pos_y + 2] = cpu
            board[pos_x][pos_y + 1] = cpu
            KI_Othello.R[pos_x][pos_y + 5] = -500
            KI_Othello.R[pos_x][pos_y + 4] = -500
            KI_Othello.R[pos_x][pos_y + 3] = -500
            KI_Othello.R[pos_x][pos_y + 2] = -500
            KI_Othello.R[pos_x][pos_y + 1] = -500
        elif spieler in board[pos_x][pos_y + 1] and spieler in board[pos_x][pos_y + 2] and spieler in board[pos_x][
            pos_y + 3] and spieler in board[pos_x][pos_y + 4] \
                and cpu in board[pos_x][pos_y + 5]:
            board[pos_x][pos_y + 4] = cpu
            board[pos_x][pos_y + 3] = cpu
            board[pos_x][pos_y + 2] = cpu
            board[pos_x][pos_y + 1] = cpu
            KI_Othello.R[pos_x][pos_y + 4] = -500
            KI_Othello.R[pos_x][pos_y + 3] = -500
            KI_Othello.R[pos_x][pos_y + 2] = -500
            KI_Othello.R[pos_x][pos_y + 1] = -500
        elif spieler in board[pos_x][pos_y + 1] and spieler in board[pos_x][pos_y + 2] and spieler in board[pos_x][pos_y + 3] \
                and cpu in board[pos_x][pos_y + 4]:
            board[pos_x][pos_y + 3] = cpu
            board[pos_x][pos_y + 2] = cpu
            board[pos_x][pos_y + 1] = cpu
            KI_Othello.R[pos_x][pos_y + 3] = -500
            KI_Othello.R[pos_x][pos_y + 2] = -500
            KI_Othello.R[pos_x][pos_y + 1] = -500
        elif spieler in board[pos_x][pos_y + 1] and spieler in board[pos_x][pos_y + 2] \
                and cpu in board[pos_x][pos_y + 3]:
            board[pos_x][pos_y + 2] = cpu
            board[pos_x][pos_y + 1] = cpu
            KI_Othello.R[pos_x][pos_y + 2] = -500
            KI_Othello.R[pos_x][pos_y + 1] = -500
        elif spieler in board[pos_x][pos_y + 1] \
                and cpu in board[pos_x][pos_y + 2]:
            board[pos_x][pos_y + 1] = cpu
            KI_Othello.R[pos_x][pos_y + 1] = -500

        # überprüfe x[0] bis x[7]
        if spieler in board[pos_x + 1][pos_y] and spieler in board[pos_x + 2][pos_y] and spieler in board[pos_x + 3][
            pos_y] and spieler in board[pos_x + 4][pos_y] \
                and spieler in board[pos_x + 5][pos_y] and spieler in board[pos_x + 6][pos_y] \
                and cpu in board[pos_x + 7][pos_y]:
            board[pos_x + 6][pos_y] = cpu
            board[pos_x + 5][pos_y] = cpu
            board[pos_x + 4][pos_y] = cpu
            board[pos_x + 3][pos_y] = cpu
            board[pos_x + 2][pos_y] = cpu
            board[pos_x + 1][pos_y] = cpu
            KI_Othello.R[pos_x + 6][pos_y] = -500
            KI_Othello.R[pos_x + 5][pos_y] = -500
            KI_Othello.R[pos_x + 4][pos_y] = -500
            KI_Othello.R[pos_x + 3][pos_y] = -500
            KI_Othello.R[pos_x + 2][pos_y] = -500
            KI_Othello.R[pos_x + 1][pos_y] = -500
        elif spieler in board[pos_x + 1][pos_y] and spieler in board[pos_x + 2][pos_y] and spieler in board[pos_x + 3][
            pos_y] and spieler in board[pos_x + 4][pos_y] \
                and spieler in board[pos_x + 5][pos_y] \
                and cpu in board[pos_x][pos_y]:
            board[pos_x + 5][pos_y] = cpu
            board[pos_x + 4][pos_y] = cpu
            board[pos_x + 3][pos_y] = cpu
            board[pos_x + 2][pos_y] = cpu
            board[pos_x + 1][pos_y] = cpu
            KI_Othello.R[pos_x + 5][pos_y] = -500
            KI_Othello.R[pos_x + 4][pos_y] = -500
            KI_Othello.R[pos_x + 3][pos_y] = -500
            KI_Othello.R[pos_x + 2][pos_y] = -500
            KI_Othello.R[pos_x + 1][pos_y] = -500
        elif spieler in board[pos_x + 1][pos_y] and spieler in board[pos_x + 2][pos_y] and spieler in board[pos_x + 3][pos_y] and spieler in board[pos_x + 4][pos_y] \
                and cpu in board[pos_x + 5][pos_y]:
            board[pos_x + 4][pos_y] = cpu
            board[pos_x + 3][pos_y] = cpu
            board[pos_x + 2][pos_y] = cpu
            board[pos_x + 1][pos_y] = cpu
            KI_Othello.R[pos_x + 4][pos_y] = -500
            KI_Othello.R[pos_x + 3][pos_y] = -500
            KI_Othello.R[pos_x + 2][pos_y] = -500
            KI_Othello.R[pos_x + 1][pos_y] = -500
        elif spieler in board[pos_x + 1][pos_y] and spieler in board[pos_x + 2][pos_y] and spieler in board[pos_x + 3][pos_y] \
                and cpu in board[pos_x + 4][pos_y]:
            board[pos_x + 3][pos_y] = cpu
            board[pos_x + 2][pos_y] = cpu
            board[pos_x + 1][pos_y] = cpu
            KI_Othello.R[pos_x + 3][pos_y] = -500
            KI_Othello.R[pos_x + 2][pos_y] = -500
            KI_Othello.R[pos_x + 1][pos_y] = -500
        elif spieler in board[pos_x + 1][pos_y] and spieler in board[pos_x + 2][pos_y] \
                and cpu in board[pos_x + 3][pos_y]:
            board[pos_x + 2][pos_y] = cpu
            board[pos_x + 1][pos_y] = cpu
            KI_Othello.R[pos_x + 2][pos_y] = -500
            KI_Othello.R[pos_x + 1][pos_y] = -500
        elif spieler in board[pos_x + 1][pos_y] \
                and cpu in board[pos_x + 2][pos_y]:
            board[pos_x + 1][pos_y] = cpu
            KI_Othello.R[pos_x + 1][pos_y] = -500

        # überprüfe x[7] bis x[0]
        if spieler in board[pos_x - 1][pos_y] and spieler in board[pos_x - 2][pos_y] and spieler in board[pos_x - 3][
            pos_y] and spieler in board[pos_x - 4][pos_y] \
                and spieler in board[pos_x - 5][pos_y] and spieler in board[pos_x - 6][pos_y] \
                and cpu in board[pos_x - 7][pos_y]:
            board[pos_x - 6][pos_y] = cpu
            board[pos_x - 5][pos_y] = cpu
            board[pos_x - 4][pos_y] = cpu
            board[pos_x - 3][pos_y] = cpu
            board[pos_x - 2][pos_y] = cpu
            board[pos_x - 1][pos_y] = cpu
            KI_Othello.R[pos_x - 6][pos_y] = -500
            KI_Othello.R[pos_x - 5][pos_y] = -500
            KI_Othello.R[pos_x - 4][pos_y] = -500
            KI_Othello.R[pos_x - 3][pos_y] = -500
            KI_Othello.R[pos_x - 2][pos_y] = -500
            KI_Othello.R[pos_x - 1][pos_y] = -500
        elif spieler in board[pos_x - 1][pos_y] and spieler in board[pos_x - 2][pos_y] and spieler in board[pos_x - 3][
            pos_y] and spieler in board[pos_x - 4][pos_y] \
                and spieler in board[pos_x - 5][pos_y] \
                and cpu in board[pos_x][pos_y]:
            board[pos_x - 5][pos_y] = cpu
            board[pos_x - 4][pos_y] = cpu
            board[pos_x - 3][pos_y] = cpu
            board[pos_x - 2][pos_y] = cpu
            board[pos_x - 1][pos_y] = cpu
            KI_Othello.R[pos_x - 5][pos_y] = -500
            KI_Othello.R[pos_x - 4][pos_y] = -500
            KI_Othello.R[pos_x - 3][pos_y] = -500
            KI_Othello.R[pos_x - 2][pos_y] = -500
            KI_Othello.R[pos_x - 1][pos_y] = -500
        elif spieler in board[pos_x - 1][pos_y] and spieler in board[pos_x - 2][pos_y] and spieler in board[pos_x - 3][
            pos_y] and spieler in board[pos_x - 4][pos_y] \
                and cpu in board[pos_x - 5][pos_y]:
            board[pos_x - 4][pos_y] = cpu
            board[pos_x - 3][pos_y] = cpu
            board[pos_x - 2][pos_y] = cpu
            board[pos_x - 1][pos_y] = cpu
            KI_Othello.R[pos_x - 4][pos_y] = -500
            KI_Othello.R[pos_x - 3][pos_y] = -500
            KI_Othello.R[pos_x - 2][pos_y] = -500
            KI_Othello.R[pos_x - 1][pos_y] = -500
        elif spieler in board[pos_x - 1][pos_y] and spieler in board[pos_x - 2][pos_y] and spieler in board[pos_x - 3][pos_y] \
                and cpu in board[pos_x - 4][pos_y]:
            board[pos_x - 3][pos_y] = cpu
            board[pos_x - 2][pos_y] = cpu
            board[pos_x - 1][pos_y] = cpu
            KI_Othello.R[pos_x - 3][pos_y] = -500
            KI_Othello.R[pos_x - 2][pos_y] = -500
            KI_Othello.R[pos_x - 1][pos_y] = -500
        elif spieler in board[pos_x - 1][pos_y] and spieler in board[pos_x - 2][pos_y] \
                and cpu in board[pos_x - 3][pos_y]:
            board[pos_x - 2][pos_y] = cpu
            board[pos_x - 1][pos_y] = cpu
            KI_Othello.R[pos_x - 2][pos_y] = -500
            KI_Othello.R[pos_x - 1][pos_y] = -500
        elif spieler in board[pos_x - 1][pos_y] \
                and cpu in board[pos_x - 2][pos_y]:
            board[pos_x - 1][pos_y] = cpu
            KI_Othello.R[pos_x - 1][pos_y] = -500

        # überprüfe x[0] bis y[0]
        if spieler in board[pos_x + 1][pos_y - 1] and spieler in board[pos_x + 2][pos_y - 2] and spieler in board[pos_x + 3][
            pos_y - 3] and spieler in board[pos_x + 4][pos_y - 4] \
                and spieler in board[pos_x + 5][pos_y - 5] and spieler in board[pos_x + 6][pos_y - 6] \
                and cpu in board[pos_x + 7][pos_y]:
            board[pos_x + 6][pos_y - 6] = cpu
            board[pos_x + 5][pos_y - 5] = cpu
            board[pos_x + 4][pos_y - 4] = cpu
            board[pos_x + 3][pos_y - 3] = cpu
            board[pos_x + 2][pos_y - 2] = cpu
            board[pos_x + 1][pos_y - 1] = cpu
            KI_Othello.R[pos_x + 6][pos_y - 6] = -500
            KI_Othello.R[pos_x + 5][pos_y - 5] = -500
            KI_Othello.R[pos_x + 4][pos_y - 4] = -500
            KI_Othello.R[pos_x + 3][pos_y - 3] = -500
            KI_Othello.R[pos_x + 2][pos_y - 2] = -500
            KI_Othello.R[pos_x + 1][pos_y - 1] = -500
        elif spieler in board[pos_x + 1][pos_y - 1] and spieler in board[pos_x + 2][pos_y - 2] and spieler in board[pos_x + 3][
            pos_y - 3] and spieler in board[pos_x + 4][pos_y - 4] \
                and spieler in board[pos_x + 5][pos_y - 5] \
                and cpu in board[pos_x][pos_y]:
            board[pos_x + 5][pos_y - 5] = cpu
            board[pos_x + 4][pos_y - 4] = cpu
            board[pos_x + 3][pos_y - 3] = cpu
            board[pos_x + 2][pos_y - 2] = cpu
            board[pos_x + 1][pos_y - 1] = cpu
            KI_Othello.R[pos_x + 5][pos_y - 5] = -500
            KI_Othello.R[pos_x + 4][pos_y - 4] = -500
            KI_Othello.R[pos_x + 3][pos_y - 3] = -500
            KI_Othello.R[pos_x + 2][pos_y - 2] = -500
            KI_Othello.R[pos_x + 1][pos_y - 1] = -500
        elif spieler in board[pos_x + 1][pos_y - 1] and spieler in board[pos_x + 2][pos_y - 2] and spieler in board[pos_x + 3][
            pos_y - 3] and spieler in board[pos_x + 4][pos_y - 4] \
                and cpu in board[pos_x + 5][pos_y - 5]:
            board[pos_x + 4][pos_y - 4] = cpu
            board[pos_x + 3][pos_y - 3] = cpu
            board[pos_x + 2][pos_y - 2] = cpu
            board[pos_x + 1][pos_y - 1] = cpu
            KI_Othello.R[pos_x + 4][pos_y - 4] = -500
            KI_Othello.R[pos_x + 3][pos_y - 3] = -500
            KI_Othello.R[pos_x + 2][pos_y - 2] = -500
            KI_Othello.R[pos_x + 1][pos_y - 1] = -500
        elif spieler in board[pos_x + 1][pos_y - 1] and spieler in board[pos_x + 2][pos_y - 2] and spieler in board[pos_x + 3][
            pos_y - 3] \
                and cpu in board[pos_x + 4][pos_y - 4]:
            board[pos_x + 3][pos_y - 3] = cpu
            board[pos_x + 2][pos_y - 2] = cpu
            board[pos_x + 1][pos_y - 1] = cpu
            KI_Othello.R[pos_x + 3][pos_y - 3] = -500
            KI_Othello.R[pos_x + 2][pos_y - 2] = -500
            KI_Othello.R[pos_x + 1][pos_y - 1] = -500
        elif spieler in board[pos_x + 1][pos_y - 1] and spieler in board[pos_x + 2][pos_y - 2] \
                and cpu in board[pos_x + 3][pos_y - 3]:
            board[pos_x + 2][pos_y - 2] = cpu
            board[pos_x + 1][pos_y - 1] = cpu
            KI_Othello.R[pos_x + 2][pos_y - 2] = -500
            KI_Othello.R[pos_x + 1][pos_y - 1] = -500          
        elif spieler in board[pos_x + 1][pos_y - 1] \
                and cpu in board[pos_x + 2][pos_y - 2]:
            board[pos_x + 1][pos_y - 1] = cpu
            KI_Othello.R[pos_x + 1][pos_y - 1] = -500
   

        # überprüfe 7,0 bis 0,7
        if spieler in board[pos_x - 1][pos_y + 1] and spieler in board[pos_x - 2][pos_y + 2] and spieler in board[pos_x - 3][
            pos_y + 3] and spieler in board[pos_x - 4][pos_y + 4] \
                and spieler in board[pos_x - 5][pos_y + 5] and spieler in board[pos_x - 6][pos_y + 6] \
                and cpu in board[pos_x - 7][pos_y]:
            board[pos_x - 6][pos_y + 6] = cpu
            board[pos_x - 5][pos_y + 5] = cpu
            board[pos_x - 4][pos_y + 4] = cpu
            board[pos_x - 3][pos_y + 3] = cpu
            board[pos_x - 2][pos_y + 2] = cpu
            board[pos_x - 1][pos_y + 1] = cpu
            KI_Othello.R[pos_x - 6][pos_y + 6] = -500
            KI_Othello.R[pos_x - 5][pos_y + 5] = -500
            KI_Othello.R[pos_x - 4][pos_y + 4] = -500
            KI_Othello.R[pos_x - 3][pos_y + 3] = -500
            KI_Othello.R[pos_x - 2][pos_y + 2] = -500
            KI_Othello.R[pos_x - 1][pos_y + 1] = -500
        elif spieler in board[pos_x - 1][pos_y + 1] and spieler in board[pos_x - 2][pos_y + 2] and spieler in board[pos_x - 3][
            pos_y + 3] and spieler in board[pos_x - 4][pos_y + 4] \
                and spieler in board[pos_x - 5][pos_y + 5] \
                and cpu in board[pos_x][pos_y]:
            board[pos_x - 5][pos_y + 5] = cpu
            board[pos_x - 4][pos_y + 4] = cpu
            board[pos_x - 3][pos_y + 3] = cpu
            board[pos_x - 2][pos_y + 2] = cpu
            board[pos_x - 1][pos_y + 1] = cpu
            KI_Othello.R[pos_x - 5][pos_y + 5] = -500
            KI_Othello.R[pos_x - 4][pos_y + 4] = -500
            KI_Othello.R[pos_x - 3][pos_y + 3] = -500
            KI_Othello.R[pos_x - 2][pos_y + 2] = -500
            KI_Othello.R[pos_x - 1][pos_y + 1] = -500
        elif spieler in board[pos_x - 1][pos_y + 1] and spieler in board[pos_x - 2][pos_y + 2] and spieler in board[pos_x - 3][
            pos_y + 3] and spieler in board[pos_x - 4][pos_y + 4] \
                and cpu in board[pos_x - 5][pos_y + 5]:
            board[pos_x - 4][pos_y + 4] = cpu
            board[pos_x - 3][pos_y + 3] = cpu
            board[pos_x - 2][pos_y + 2] = cpu
            board[pos_x - 1][pos_y + 1] = cpu
            KI_Othello.R[pos_x - 4][pos_y + 4] = -500
            KI_Othello.R[pos_x - 3][pos_y + 3] = -500
            KI_Othello.R[pos_x - 2][pos_y + 2] = -500
            KI_Othello.R[pos_x - 1][pos_y + 1] = -500
        elif spieler in board[pos_x - 1][pos_y + 1] and spieler in board[pos_x - 2][pos_y + 2] and spieler in board[pos_x - 3][
            pos_y + 3] \
                and cpu in board[pos_x - 4][pos_y + 4]:
            board[pos_x - 3][pos_y + 3] = cpu
            board[pos_x - 2][pos_y + 2] = cpu
            board[pos_x - 1][pos_y + 1] = cpu
            KI_Othello.R[pos_x - 3][pos_y + 3] = -500
            KI_Othello.R[pos_x - 2][pos_y + 2] = -500
            KI_Othello.R[pos_x - 1][pos_y + 1] = -500
        elif spieler in board[pos_x - 1][pos_y + 1] and spieler in board[pos_x - 2][pos_y + 2] \
                and cpu in board[pos_x - 3][pos_y + 3]:
            board[pos_x - 2][pos_y + 2] = cpu
            board[pos_x - 1][pos_y + 1] = cpu
            KI_Othello.R[pos_x - 2][pos_y + 2] = -500
            KI_Othello.R[pos_x - 1][pos_y + 1] = -500
        elif spieler in board[pos_x - 1][pos_y + 1] \
                and cpu in board[pos_x - 2][pos_y + 2]:
            board[pos_x - 1][pos_y + 1] = cpu
            KI_Othello.R[pos_x - 1][pos_y + 1] = -500

        # überprüfe 7,0 bis 0,0
        if spieler in board[pos_x - 1][pos_y - 1] and spieler in board[pos_x - 2][pos_y - 2] and spieler in board[pos_x - 3][
            pos_y - 3] and spieler in board[pos_x - 4][pos_y - 4] \
                and spieler in board[pos_x - 5][pos_y - 5] and spieler in board[pos_x - 6][pos_y - 6] \
                and cpu in board[pos_x - 7][pos_y]:
            board[pos_x - 6][pos_y - 6] = cpu
            board[pos_x - 5][pos_y - 5] = cpu
            board[pos_x - 4][pos_y - 4] = cpu
            board[pos_x - 3][pos_y - 3] = cpu
            board[pos_x - 2][pos_y - 2] = cpu
            board[pos_x - 1][pos_y - 1] = cpu
            KI_Othello.R[pos_x - 6][pos_y - 6] = -500
            KI_Othello.R[pos_x - 5][pos_y - 5] = -500
            KI_Othello.R[pos_x - 4][pos_y - 4] = -500
            KI_Othello.R[pos_x - 3][pos_y - 3] = -500
            KI_Othello.R[pos_x - 2][pos_y - 2] = -500
            KI_Othello.R[pos_x - 1][pos_y - 1] = -500
        elif spieler in board[pos_x - 1][pos_y - 1] and spieler in board[pos_x - 2][pos_y - 2] and spieler in board[pos_x - 3][
            pos_y - 3] and spieler in board[pos_x - 4][pos_y - 4] \
                and spieler in board[pos_x - 5][pos_y - 5] \
                and cpu in board[pos_x][pos_y]:
            board[pos_x - 5][pos_y - 5] = cpu
            board[pos_x - 4][pos_y - 4] = cpu
            board[pos_x - 3][pos_y - 3] = cpu
            board[pos_x - 2][pos_y - 2] = cpu
            board[pos_x - 1][pos_y - 1] = cpu
            KI_Othello.R[pos_x - 5][pos_y - 5] = -500
            KI_Othello.R[pos_x - 4][pos_y - 4] = -500
            KI_Othello.R[pos_x - 3][pos_y - 3] = -500
            KI_Othello.R[pos_x - 2][pos_y - 2] = -500
            KI_Othello.R[pos_x - 1][pos_y - 1] = -500
        elif spieler in board[pos_x - 1][pos_y - 1] and spieler in board[pos_x - 2][pos_y - 2] and spieler in board[pos_x - 3][
            pos_y - 3] and spieler in board[pos_x - 4][pos_y - 4] \
                and cpu in board[pos_x - 5][pos_y - 5]:
            board[pos_x - 4][pos_y - 4] = cpu
            board[pos_x - 3][pos_y - 3] = cpu
            board[pos_x - 2][pos_y - 2] = cpu
            board[pos_x - 1][pos_y - 1] = cpu
            KI_Othello.R[pos_x - 4][pos_y - 4] = -500
            KI_Othello.R[pos_x - 3][pos_y - 3] = -500
            KI_Othello.R[pos_x - 2][pos_y - 2] = -500
            KI_Othello.R[pos_x - 1][pos_y - 1] = -500
        elif spieler in board[pos_x - 1][pos_y - 1] and spieler in board[pos_x - 2][pos_y - 2] and spieler in board[pos_x - 3][
            pos_y - 3] \
                and cpu in board[pos_x - 4][pos_y - 4]:
            board[pos_x - 3][pos_y - 3] = cpu
            board[pos_x - 2][pos_y - 2] = cpu
            board[pos_x - 1][pos_y - 1] = cpu
            KI_Othello.R[pos_x - 3][pos_y - 3] = -500
            KI_Othello.R[pos_x - 2][pos_y - 2] = -500
            KI_Othello.R[pos_x - 1][pos_y - 1] = -500
        elif spieler in board[pos_x - 1][pos_y - 1] and spieler in board[pos_x - 2][pos_y - 2] \
                and cpu in board[pos_x - 3][pos_y - 3]:
            board[pos_x - 2][pos_y - 2] = cpu
            board[pos_x - 1][pos_y - 1] = cpu
            KI_Othello.R[pos_x - 2][pos_y - 2] = -500
            KI_Othello.R[pos_x - 1][pos_y - 1] = -500
        elif spieler in board[pos_x - 1][pos_y - 1] \
                and cpu in board[pos_x - 2][pos_y - 2]:
            board[pos_x - 1][pos_y - 1] = cpu
            KI_Othello.R[pos_x - 1][pos_y - 1] = -500

        # überprüfe x+ y+
        if spieler in board[pos_x + 1][pos_y + 1] and spieler in board[pos_x + 2][pos_y + 2] and spieler in board[pos_x + 3][
            pos_y + 3] and spieler in board[pos_x + 4][pos_y + 4] \
                and spieler in board[pos_x + 5][pos_y + 5] and spieler in board[pos_x + 6][pos_y + 6] \
                and cpu in board[pos_x + 7][pos_y]:
            board[pos_x + 6][pos_y + 6] = cpu
            board[pos_x + 5][pos_y + 5] = cpu
            board[pos_x + 4][pos_y + 4] = cpu
            board[pos_x + 3][pos_y + 3] = cpu
            board[pos_x + 2][pos_y + 2] = cpu
            board[pos_x + 1][pos_y + 1] = cpu
            KI_Othello.R[pos_x + 6][pos_y + 6] = -500
            KI_Othello.R[pos_x + 5][pos_y + 5] = -500
            KI_Othello.R[pos_x + 4][pos_y + 4] = -500
            KI_Othello.R[pos_x + 3][pos_y + 3] = -500
            KI_Othello.R[pos_x + 2][pos_y + 2] = -500
            KI_Othello.R[pos_x + 1][pos_y + 1] = -500
        elif spieler in board[pos_x + 1][pos_y + 1] and spieler in board[pos_x + 2][pos_y + 2] and spieler in board[pos_x + 3][
            pos_y + 3] and spieler in board[pos_x + 4][pos_y + 4] \
                and spieler in board[pos_x + 5][pos_y + 5] \
                and cpu in board[pos_x][pos_y]:
            board[pos_x + 5][pos_y + 5] = cpu
            board[pos_x + 4][pos_y + 4] = cpu
            board[pos_x + 3][pos_y + 3] = cpu
            board[pos_x + 2][pos_y + 2] = cpu
            board[pos_x + 1][pos_y + 1] = cpu
            KI_Othello.R[pos_x + 5][pos_y + 5] = -500
            KI_Othello.R[pos_x + 4][pos_y + 4] = -500
            KI_Othello.R[pos_x + 3][pos_y + 3] = -500
            KI_Othello.R[pos_x + 2][pos_y + 2] = -500
            KI_Othello.R[pos_x + 1][pos_y + 1] = -500
        elif spieler in board[pos_x + 1][pos_y + 1] and spieler in board[pos_x + 2][pos_y + 2] and spieler in board[pos_x + 3][
            pos_y + 3] and spieler in board[pos_x + 4][pos_y + 4] \
                and cpu in board[pos_x + 5][pos_y + 5]:
            board[pos_x + 4][pos_y + 4] = cpu
            board[pos_x + 3][pos_y + 3] = cpu
            board[pos_x + 2][pos_y + 2] = cpu
            board[pos_x + 1][pos_y + 1] = cpu
            KI_Othello.R[pos_x + 4][pos_y + 4] = -500
            KI_Othello.R[pos_x + 3][pos_y + 3] = -500
            KI_Othello.R[pos_x + 2][pos_y + 2] = -500
            KI_Othello.R[pos_x + 1][pos_y + 1] = -500
        elif spieler in board[pos_x + 1][pos_y + 1] and spieler in board[pos_x + 2][pos_y + 2] and spieler in board[pos_x + 3][
            pos_y + 3] \
                and cpu in board[pos_x + 4][pos_y + 4]:
            board[pos_x + 3][pos_y + 3] = cpu
            board[pos_x + 2][pos_y + 2] = cpu
            board[pos_x + 1][pos_y + 1] = cpu
            KI_Othello.R[pos_x + 3][pos_y + 3] = -500
            KI_Othello.R[pos_x + 2][pos_y + 2] = -500
            KI_Othello.R[pos_x + 1][pos_y + 1] = -500
        elif spieler in board[pos_x + 1][pos_y + 1] and spieler in board[pos_x + 2][pos_y + 2] \
                and cpu in board[pos_x + 3][pos_y + 3]:
            board[pos_x + 2][pos_y + 2] = cpu
            board[pos_x + 1][pos_y + 1] = cpu
            KI_Othello.R[pos_x + 2][pos_y + 2] = -500
            KI_Othello.R[pos_x + 1][pos_y + 1] = -500
        elif spieler in board[pos_x + 1][pos_y + 1] \
                and cpu in board[pos_x + 2][pos_y + 2]:
            board[pos_x + 1][pos_y + 1] = cpu
            KI_Othello.R[pos_x + 1][pos_y + 1] = -500
    except:
        print("Dieser Zug ist nicht möglich")
        cpuZieht(board, cpu, start)

    print()

def cpuZieht(board, cpu, start):
    # ermittle die Felder, auf die die KI Steine setzen kann
    arr_player = [] # leeres Array für die aktuellen Spielersteine erstellen
    arr_cpu = []    # leeres Array für die aktuellen KI-Steine erstellen
    for x in range(0,9):
        for y in range(0,9):
            if board[x][y] == spieler:
               arr_player.append([x,y])
            elif board[x][y] == cpu:
                arr_cpu.append([x,y])

    # ermittle die freien Felder, die von der KI gespielt werden können
    # -500 -> Feld belegt, 100 -> Feld ist frei und kann gespielt werden, 200 -> Feld ist frei und es können mehrere fremde Steine eingeschlossen werden
    for x in range(len(arr_player)):
        z = arr_player[x]
        Pos_X = z[0]
        Pos_Y = z[1]
        try:
            # 1 Spielerstein dazwischen
            if Pos_X > 0 and Pos_Y > 0:
                if board[Pos_X - 1][Pos_Y - 1] == cpu and KI_Othello.R[Pos_X + 1][Pos_Y + 1] != -500:
                    KI_Othello.R[Pos_X + 1][Pos_Y + 1] = 103
                if board[Pos_X][Pos_Y - 1] == cpu and KI_Othello.R[Pos_X][Pos_Y + 1] != -500:
                    KI_Othello.R[Pos_X][Pos_Y + 1] = 102
                if board[Pos_X - 1][Pos_Y] == cpu and KI_Othello.R[Pos_X + 1][Pos_Y] != -500:
                    KI_Othello.R[Pos_X + 1][Pos_Y] = 101

            if Pos_X > 0 and Pos_Y < 7:
                if board[Pos_X - 1][Pos_Y + 1] == cpu and KI_Othello.R[Pos_X + 1][Pos_Y - 1] != -500:
                        KI_Othello.R[Pos_X + 1][Pos_Y - 1] = 104
                if board[Pos_X][Pos_Y + 1] == cpu and KI_Othello.R[Pos_X][Pos_Y - 1] != -500:
                    KI_Othello.R[Pos_X][Pos_Y - 1] = 102

            if Pos_X < 7 and Pos_Y < 7:
                if board[Pos_X + 1][Pos_Y + 1] == cpu and KI_Othello.R[Pos_X - 1][Pos_Y - 1] != -500:
                    KI_Othello.R[Pos_X - 1][Pos_Y - 1] = 103
                if board[Pos_X + 1][Pos_Y - 1] == cpu and KI_Othello.R[Pos_X - 1][Pos_Y + 1] != -500:
                    KI_Othello.R[Pos_X - 1][Pos_Y + 1] = 104
                if board[Pos_X + 1][Pos_Y] == cpu and KI_Othello.R[Pos_X - 1][Pos_Y] != -500:
                    KI_Othello.R[Pos_X - 1][Pos_Y] = 101

            # 2 Spielersteine dazwischen
            if board[Pos_X][Pos_Y + 1] == spieler and board[Pos_X][Pos_Y + 2] == cpu and KI_Othello.R[Pos_X][Pos_Y - 1] != -500:
                KI_Othello.R[Pos_X][Pos_Y - 1] = 201
            if board[Pos_X][Pos_Y + 1] == spieler and board[Pos_X][Pos_Y - 1] == cpu and KI_Othello.R[Pos_X][Pos_Y + 2] != -500:
                KI_Othello.R[Pos_X][Pos_Y + 2] = 201
            if board[Pos_X][Pos_Y - 1] == spieler and board[Pos_X][Pos_Y - 2] == cpu and KI_Othello.R[Pos_X][Pos_Y + 1] != -500:
                KI_Othello.R[Pos_X][Pos_Y + 1] = 202
            if board[Pos_X][Pos_Y - 1] == spieler and board[Pos_X][Pos_Y + 1] == cpu and KI_Othello.R[Pos_X][Pos_Y - 2] != -500:
                KI_Othello.R[Pos_X][Pos_Y - 2] = 202
            if board[Pos_X+1][Pos_Y] == spieler and board[Pos_X+2][Pos_Y] == cpu and KI_Othello.R[Pos_X][Pos_Y + 1] != -500:
                KI_Othello.R[Pos_X][Pos_Y + 1] = 203
            if board[Pos_X+1][Pos_Y] == spieler and board[Pos_X - 1][Pos_Y] == cpu and KI_Othello.R[Pos_X+2][Pos_Y] != -500:
                KI_Othello.R[Pos_X + 2][Pos_Y] = 203
            if board[Pos_X-1][Pos_Y] == spieler and board[Pos_X-2][Pos_Y] == cpu and KI_Othello.R[Pos_X][Pos_Y - 1] != -500:
                KI_Othello.R[Pos_X][Pos_Y - 1] = 204
            if board[Pos_X-1][Pos_Y] == spieler and board[Pos_X][Pos_Y - 1] == cpu and KI_Othello.R[Pos_X - 2][Pos_Y] != -500:
                KI_Othello.R[Pos_X - 2][Pos_Y] = 204
            if board[Pos_X+1][Pos_Y + 1] == spieler and board[Pos_X+2][Pos_Y + 2] == cpu and KI_Othello.R[Pos_X-1][Pos_Y - 1] != -500:
                KI_Othello.R[Pos_X-1][Pos_Y - 1] = 205
            if board[Pos_X+1][Pos_Y + 1] == spieler and board[Pos_X - 1][Pos_Y - 1] == cpu and KI_Othello.R[Pos_X + 2][Pos_Y + 2] != -500:
                KI_Othello.R[Pos_X + 2][Pos_Y + 2] = 205
            if board[Pos_X+1][Pos_Y - 1] == spieler and board[Pos_X+2][Pos_Y - 2] == cpu and KI_Othello.R[Pos_X-1][Pos_Y + 1] != -500:
                KI_Othello.R[Pos_X-1][Pos_Y + 1] = 206
            if board[Pos_X+1][Pos_Y - 1] == spieler and board[Pos_X - 1][Pos_Y + 1] == cpu and KI_Othello.R[Pos_X + 2][Pos_Y - 2] != -500:
                KI_Othello.R[Pos_X + 2][Pos_Y - 2] = 206
            if board[Pos_X - 1][Pos_Y + 1] == spieler and board[Pos_X - 2][Pos_Y + 2] == cpu and KI_Othello.R[Pos_X + 1][Pos_Y - 1] != -500:
                KI_Othello.R[Pos_X + 1][Pos_Y - 1] = 207
            if board[Pos_X - 1][Pos_Y + 1] == spieler and board[Pos_X + 1][Pos_Y - 1] == cpu and KI_Othello.R[Pos_X - 2][Pos_Y + 2] != -500:
                KI_Othello.R[Pos_X - 2][Pos_Y + 2] = 207
            if board[Pos_X - 1][Pos_Y - 1] == spieler and board[Pos_X - 2][Pos_Y - 2] == cpu and KI_Othello.R[Pos_X + 1][Pos_Y + 1] != -500:
                KI_Othello.R[Pos_X + 1][Pos_Y + 1] = 208
            if board[Pos_X - 1][Pos_Y - 1] == spieler and board[Pos_X + 1][Pos_Y + 1] == cpu and KI_Othello.R[Pos_X - 2][Pos_Y - 2] != -500:
                KI_Othello.R[Pos_X - 2][Pos_Y - 2] = 208

            # 3 Spielersteine dazwischen
            if board[Pos_X + 1][Pos_Y] == spieler and board[Pos_X + 2][Pos_Y] == spieler and board[Pos_X - 1][Pos_Y] == cpu and KI_Othello.R[Pos_X + 3][Pos_Y] != -500:
                KI_Othello.R[Pos_X + 3][Pos_Y] = 301
            if board[Pos_X + 1][Pos_Y] == spieler and board[Pos_X + 2][Pos_Y] == spieler and board[Pos_X + 3][Pos_Y] == cpu and KI_Othello.R[Pos_X - 1][Pos_Y] != -500:
                KI_Othello.R[Pos_X - 1][Pos_Y] = 301
            if board[Pos_X - 1][Pos_Y] == spieler and board[Pos_X - 2][Pos_Y] == spieler and board[Pos_X + 1][Pos_Y] == cpu and KI_Othello.R[Pos_X - 3][Pos_Y] != -500:
                KI_Othello.R[Pos_X - 3][Pos_Y] = 302
            if board[Pos_X - 1][Pos_Y] == spieler and board[Pos_X - 2][Pos_Y] == spieler and board[Pos_X - 3][Pos_Y] == cpu and KI_Othello.R[Pos_X + 1][Pos_Y] != -500:
                KI_Othello.R[Pos_X + 1][Pos_Y] = 302
            if board[Pos_X][Pos_Y + 1] == spieler and board[Pos_X][Pos_Y + 2] == spieler and board[Pos_X][Pos_Y - 1] == cpu and KI_Othello.R[Pos_X][Pos_Y + 3] != -500:
                KI_Othello.R[Pos_X][Pos_Y + 3] = 303
            if board[Pos_X][Pos_Y + 1] == spieler and board[Pos_X][Pos_Y + 2] == spieler and board[Pos_X][Pos_Y + 3] == cpu and KI_Othello.R[Pos_X][Pos_Y - 1] != -500:
                KI_Othello.R[Pos_X][Pos_Y - 1] = 303
            if board[Pos_X][Pos_Y - 1] == spieler and board[Pos_X][Pos_Y - 2] == spieler and board[Pos_X][Pos_Y + 1] == cpu and KI_Othello.R[Pos_X][Pos_Y - 3] != -500:
                KI_Othello.R[Pos_X][Pos_Y - 3] = 304
            if board[Pos_X][Pos_Y - 1] == spieler and board[Pos_X][Pos_Y - 2] == spieler and board[Pos_X][Pos_Y - 3] == cpu and KI_Othello.R[Pos_X][Pos_Y + 1] != -500:
                KI_Othello.R[Pos_X][Pos_Y + 1] = 304
            if board[Pos_X - 1][Pos_Y - 1] == spieler and board[Pos_X - 2][Pos_Y - 2] == spieler and board[Pos_X + 1][Pos_Y + 1] == cpu and KI_Othello.R[Pos_X - 3][Pos_Y - 3] != -500:
                KI_Othello.R[Pos_X - 3][Pos_Y - 3] = 305
            if board[Pos_X - 1][Pos_Y - 1] == spieler and board[Pos_X - 2][Pos_Y - 2] == spieler and board[Pos_X - 3][Pos_Y - 3] == cpu and KI_Othello.R[Pos_X + 1][Pos_Y + 1] != -500:
                KI_Othello.R[Pos_X + 1][Pos_Y + 1] = 305
            if board[Pos_X - 1][Pos_Y + 1] == spieler and board[Pos_X - 2][Pos_Y + 2] == spieler and board[Pos_X + 1][Pos_Y - 1] == cpu and KI_Othello.R[Pos_X - 3][Pos_Y + 3] != -500:
                KI_Othello.R[Pos_X - 3][Pos_Y + 3] = 306
            if board[Pos_X - 1][Pos_Y + 1] == spieler and board[Pos_X - 2][Pos_Y + 2] == spieler and board[Pos_X - 3][Pos_Y + 3] == cpu and KI_Othello.R[Pos_X + 1][Pos_Y - 1] != -500:
                KI_Othello.R[Pos_X + 1][Pos_Y - 1] = 306
            if board[Pos_X + 1][Pos_Y - 1] == spieler and board[Pos_X + 2][Pos_Y - 2] == spieler and board[Pos_X - 1][Pos_Y + 1] == cpu and KI_Othello.R[Pos_X + 3][Pos_Y - 3] != -500:
                KI_Othello.R[Pos_X + 3][Pos_Y - 3] = 307
            if board[Pos_X + 1][Pos_Y - 1] == spieler and board[Pos_X + 2][Pos_Y - 2] == spieler and board[Pos_X + 3][Pos_Y - 3] == cpu and KI_Othello.R[Pos_X - 1][Pos_Y + 1] != -500:
                KI_Othello.R[Pos_X - 1][Pos_Y + 1] = 307
            if board[Pos_X + 1][Pos_Y + 1] == spieler and board[Pos_X + 2][Pos_Y + 2] == spieler and board[Pos_X - 1][Pos_Y - 1] == cpu and KI_Othello.R[Pos_X + 3][Pos_Y + 3] != -500:
                KI_Othello.R[Pos_X + 3][Pos_Y + 3] = 308
            if board[Pos_X + 1][Pos_Y + 1] == spieler and board[Pos_X + 2][Pos_Y + 2] == spieler and board[Pos_X + 3][Pos_Y + 3] == cpu and KI_Othello.R[Pos_X - 1][Pos_Y - 1] != -500:
                KI_Othello.R[Pos_X - 1][Pos_Y - 1] = 308

            # 4 Spielersteine dazwischen
            if board[Pos_X+1][Pos_Y+1] == spieler and board[Pos_X+2][Pos_Y+2] == spieler and board[Pos_X+3][Pos_Y+3] == spieler and board[Pos_X-1][Pos_Y-1] == cpu and KI_Othello.R[Pos_X+4][Pos_Y+4] != -500:
                if Pos_X + 4 or Pos_Y + 4 > 7:
                    KI_Othello.R[Pos_X + 4][Pos_Y + 4] = 401
            if board[Pos_X+1][Pos_Y-1] == spieler and board[Pos_X+2][Pos_Y-2] == spieler and board[Pos_X+3][Pos_Y-3] == spieler and board[Pos_X-1][Pos_Y+1] == cpu and KI_Othello.R[Pos_X+4][Pos_Y-4] != -500:
                KI_Othello.R[Pos_X+4][Pos_Y-4] = 402
            if board[Pos_X][Pos_Y-1] == spieler and board[Pos_X][Pos_Y-2] == spieler and board[Pos_X][Pos_Y-3] == spieler and board[Pos_X][Pos_Y+1] == cpu and KI_Othello.R[Pos_X][Pos_Y-4] != -500:
                KI_Othello.R[Pos_X][Pos_Y-4] = 403
            if board[Pos_X][Pos_Y+1] == spieler and board[Pos_X][Pos_Y+2] == spieler and board[Pos_X][Pos_Y+3] == spieler and board[Pos_X][Pos_Y-1] == cpu and KI_Othello.R[Pos_X][Pos_Y+4] != -500:
                KI_Othello.R[Pos_X][Pos_Y+4] = 404
            if board[Pos_X-1][Pos_Y+1] == spieler and board[Pos_X-2][Pos_Y+2] == spieler and board[Pos_X-3][Pos_Y+3] == spieler and board[Pos_X+1][Pos_Y-1] == cpu and KI_Othello.R[Pos_X-4][Pos_Y+4] != -500:
                KI_Othello.R[Pos_X-4][Pos_Y+4] = 405
            if board[Pos_X-1][Pos_Y-1] == spieler and board[Pos_X-2][Pos_Y-2] == spieler and board[Pos_X-3][Pos_Y-3] == spieler and board[Pos_X+1][Pos_Y+1] == cpu and KI_Othello.R[Pos_X-4][Pos_Y-4] != -500:
                if Pos_X-4 >=4 and Pos_Y-4 >=4:
                    KI_Othello.R[Pos_X-4][Pos_Y-4] = 406
            if board[Pos_X-1][Pos_Y] == spieler and board[Pos_X-2][Pos_Y] == spieler and board[Pos_X-3][Pos_Y] == spieler and board[Pos_X+1][Pos_Y] == cpu and KI_Othello.R[Pos_X-4][Pos_Y] != -500:
                KI_Othello.R[Pos_X-4][Pos_Y] = 407
            if board[Pos_X+1][Pos_Y] == spieler and board[Pos_X+2][Pos_Y] == spieler and board[Pos_X+3][Pos_Y] == spieler and board[Pos_X-1][Pos_Y] == cpu and KI_Othello.R[Pos_X + 4][Pos_Y] != -500:
                KI_Othello.R[Pos_X + 4][Pos_Y] = 408

            # 5 Spielersteine dazwischen
            if board[Pos_X+1][Pos_Y+1] == spieler and board[Pos_X+2][Pos_Y+2] == spieler and board[Pos_X+3][Pos_Y+3] == spieler and board[Pos_X+4][Pos_Y+4] == spieler and board[Pos_X-1][Pos_Y-1] == cpu and KI_Othello.R[Pos_X+5][Pos_Y+5] != -500:
                KI_Othello.R[Pos_X+5][Pos_Y+5] = 501
            if board[Pos_X+1][Pos_Y-1] == spieler and board[Pos_X+2][Pos_Y-2] == spieler and board[Pos_X+3][Pos_Y-3] == spieler and board[Pos_X+4][Pos_Y-4] == spieler and board[Pos_X-1][Pos_Y+1] == cpu and KI_Othello.R[Pos_X+5][Pos_Y-5] != -500:
                KI_Othello.R[Pos_X+5][Pos_Y-5] = 502
            if board[Pos_X][Pos_Y-1] == spieler and board[Pos_X][Pos_Y-2] == spieler and board[Pos_X][Pos_Y-3] == spieler and board[Pos_X][Pos_Y-4] == spieler and board[Pos_X][Pos_Y+1] == cpu and KI_Othello.R[Pos_X][Pos_Y-5] != -500:
                KI_Othello.R[Pos_X][Pos_Y-5] = 503
            if board[Pos_X][Pos_Y+1] == spieler and board[Pos_X][Pos_Y+2] == spieler and board[Pos_X][Pos_Y+3] == spieler and board[Pos_X][Pos_Y+4] == spieler and board[Pos_X][Pos_Y-1] == cpu and KI_Othello.R[Pos_X][Pos_Y+5] != -500:
                KI_Othello.R[Pos_X][Pos_Y+5] = 504
            if board[Pos_X-1][Pos_Y+1] == spieler and board[Pos_X-2][Pos_Y+2] == spieler and board[Pos_X-3][Pos_Y+3] == spieler and board[Pos_X-4][Pos_Y+4] == spieler and board[Pos_X+1][Pos_Y-1] == cpu and KI_Othello.R[Pos_X-5][Pos_Y+5] != -500:
                KI_Othello.R[Pos_X-5][Pos_Y+5] = 505
            if board[Pos_X-1][Pos_Y-1] == spieler and board[Pos_X-2][Pos_Y-2] == spieler and board[Pos_X-3][Pos_Y-3] == spieler and board[Pos_X-4][Pos_Y-4] == spieler and board[Pos_X+1][Pos_Y+1] == cpu and KI_Othello.R[Pos_X-5][Pos_Y-5] != -500:
                KI_Othello.R[Pos_X-5][Pos_Y-5] = 506
            if board[Pos_X-1][Pos_Y] == spieler and board[Pos_X-2][Pos_Y] == spieler and board[Pos_X-3][Pos_Y] == spieler and board[Pos_X-4][Pos_Y] == spieler and board[Pos_X+1][Pos_Y] == cpu and KI_Othello.R[Pos_X-5][Pos_Y] != -500:
                KI_Othello.R[Pos_X-5][Pos_Y] = 507
            if board[Pos_X+1][Pos_Y] == spieler and board[Pos_X+2][Pos_Y] == spieler and board[Pos_X+3][Pos_Y] == spieler and board[Pos_X+4][Pos_Y] == spieler and board[Pos_X-1][Pos_Y] == cpu and KI_Othello.R[Pos_X + 5][Pos_Y] != -500:
                KI_Othello.R[Pos_X + 5][Pos_Y] = 508

            # 6 Spielersteine dazwischen
            if board[Pos_X + 1][Pos_Y + 1] == spieler and board[Pos_X + 2][Pos_Y + 2] == spieler and \
                    board[Pos_X + 3][Pos_Y + 3] == spieler and board[Pos_X + 4][Pos_Y + 4] == spieler and board[Pos_X + 5][Pos_Y + 5] == spieler and \
                    board[Pos_X - 1][Pos_Y - 1] == cpu and KI_Othello.R[Pos_X + 6][Pos_Y + 6] != -500:
                KI_Othello.R[Pos_X + 5][Pos_Y + 5] = 601
            if board[Pos_X + 1][Pos_Y - 1] == spieler and board[Pos_X + 2][Pos_Y - 2] == spieler and \
                    board[Pos_X + 3][Pos_Y - 3] == spieler and board[Pos_X + 4][Pos_Y - 4] == spieler and board[Pos_X + 5][Pos_Y - 5] == spieler and \
                    board[Pos_X - 1][Pos_Y + 1] == cpu and KI_Othello.R[Pos_X + 6][Pos_Y - 6] != -500:
                KI_Othello.R[Pos_X + 6][Pos_Y - 6] = 602
            if board[Pos_X][Pos_Y - 1] == spieler and board[Pos_X][Pos_Y - 2] == spieler and board[Pos_X][
                Pos_Y - 3] == spieler and board[Pos_X][Pos_Y - 4] == spieler and board[Pos_X][Pos_Y - 5] == spieler and board[Pos_X][Pos_Y + 1] == cpu and \
                    KI_Othello.R[Pos_X][Pos_Y - 6] != -500:
                KI_Othello.R[Pos_X][Pos_Y - 6] = 603
            if board[Pos_X][Pos_Y + 1] == spieler and board[Pos_X][Pos_Y + 2] == spieler and board[Pos_X][
                Pos_Y + 3] == spieler and board[Pos_X][Pos_Y + 4] == spieler and board[Pos_X][Pos_Y + 5] == spieler and board[Pos_X][Pos_Y - 1] == cpu and \
                    KI_Othello.R[Pos_X][Pos_Y + 6] != -500:
                KI_Othello.R[Pos_X][Pos_Y + 6] = 604
            if board[Pos_X - 1][Pos_Y + 1] == spieler and board[Pos_X - 2][Pos_Y + 2] == spieler and \
                    board[Pos_X - 3][Pos_Y + 3] == spieler and board[Pos_X - 4][Pos_Y + 4] == spieler and board[Pos_X - 5][Pos_Y + 5] == spieler and \
                    board[Pos_X + 1][Pos_Y - 1] == cpu and KI_Othello.R[Pos_X - 6][Pos_Y + 6] != -500:
                KI_Othello.R[Pos_X - 6][Pos_Y + 6] = 605
            if board[Pos_X - 1][Pos_Y - 1] == spieler and board[Pos_X - 2][Pos_Y - 2] == spieler and \
                    board[Pos_X - 3][Pos_Y - 3] == spieler and board[Pos_X - 4][Pos_Y - 4] == spieler and board[Pos_X - 5][Pos_Y - 5] == spieler and \
                    board[Pos_X + 1][Pos_Y + 1] == cpu and KI_Othello.R[Pos_X - 6][Pos_Y - 6] != -500:
                KI_Othello.R[Pos_X - 6][Pos_Y - 6] = 606
            if board[Pos_X - 1][Pos_Y] == spieler and board[Pos_X - 2][Pos_Y] == spieler and board[Pos_X - 3][
                Pos_Y] == spieler and board[Pos_X - 4][Pos_Y] == spieler and board[Pos_X - 5][Pos_Y] == spieler and board[Pos_X + 1][Pos_Y] == cpu and \
                    KI_Othello.R[Pos_X - 6][Pos_Y] != -500:
                KI_Othello.R[Pos_X - 6][Pos_Y] = 607
            if board[Pos_X + 1][Pos_Y] == spieler and board[Pos_X + 2][Pos_Y] == spieler and board[Pos_X + 3][
                Pos_Y] == spieler and board[Pos_X + 4][Pos_Y] == spieler and board[Pos_X + 5][Pos_Y] == spieler and board[Pos_X - 1][Pos_Y] == cpu and \
                    KI_Othello.R[Pos_X + 6][Pos_Y] != -500:
                KI_Othello.R[Pos_X + 6][Pos_Y] = 608
        except ValueError:
            print("keine gültige Zahl.")
        except ZeroDivisionError:
            print("Division durch 0 nicht möglich")
            pass
        except KeyError:
            print("KeyError")
            pass
        except FloatingPointError:
            print("FloatingPointError")
            pass
        except IndexError:
            #print("Indexerror")
            #print(Pos_X, Pos_Y)
            pass
        except:
            print("Unbekannter Fehler:"), sys.exc_info()[0]
            #spielerZieht(board, False)
            pass

    # Finale Q-Matrix normalisieren und anzeigen
    # #print(np.round(Q / np.max(Q), 8))

    # Anwort der KI (array(x, y))
    try:
        # Q-Learning
        RKI = KI_Othello.R
        Q = KI_Othello.q_learning(R=RKI, gamma=0.95, alpha=0.8, episodes=1000)
        KI_Othello.R = RKI
        #print(list(zip(*np.where(np.round(Q / np.max(Q) == 1)))))
        KIZug = list(zip(*np.where(np.round(Q / np.max(Q) == 1))))
        for x in range(len(KIZug)):
            x = KIZug[x]
            Pos_X = x[0]
            Pos_Y = x[1]
        KI_Othello.R[Pos_X][Pos_Y] = -500
        spielerSteineDrehen(theBoard, Pos_X, Pos_Y, cpu, spieler)
        theBoard[Pos_X][Pos_Y] = cpu
    except:
        print("Index außerhalb des Bretts!!")

    # Matrix bereinigen
    for z in range(0,8):
        for s in range(0,8):
            if KI_Othello.R[z][s] != -500:
                KI_Othello.R[z][s] = -200

    drawBoard(theBoard)
    spielstand(theBoard)

def spielerZieht(board, start):
    global runCPU
    global runPlayer
    spielerzug = input("Bitte Zug durch Komma getrennt eingeben(x,y):")
    spielerzug = spielerzug.split(',')
    pos_x = int(spielerzug[0])
    pos_y = int(spielerzug[1])
    #print("Ihre Eingabe x = ", pos_x)
    #print("Ihre Eingabe y = ", pos_y)
    pruefeGueltigenSpielerZug(board,pos_x,pos_y)
    KI_Othello.R[pos_x][pos_y] = -500
    runCPU = True
    runPlayer = False
    return board

def spielstand(board):
    counter_X = 0
    counter_O = 0
    for zeilen in range(len(board)):
        for spalten in range(len(board)):
            if board[spalten][zeilen] == 'X':
                counter_X += 1
            elif (board[spalten][zeilen] == 'O'):
                counter_O +=1
    if cpu == 'X' and counter_X > counter_O:
        print("Die KI führt mit %u zu %u" %(counter_X, counter_O))
    if cpu == 'O' and counter_O > counter_X:
        print("Die KI führt mit %u zu %u" %(counter_O, counter_X))
    if spieler == 'X' and counter_X > counter_O:
        print("Du führst mit %u zu %u" %(counter_X, counter_O))
    if counter_X == counter_O:
        print("Es steht %u zu %u" %(counter_X, counter_O))
    if counter_O + counter_X == 64:
        print("Das Spiel ist zu Ende")
        runPlayer = False
        runCPU = False
        os._exit(0)

# Spielablauf

print('Willkommen zu O T H E L L O by Harald Wörl (2020)')
print()
print('Wollen Sie mit X (schwarz) oder mit O (weiß) spielen ?')
print('X beginnt')
spieler = input()
if spieler == 'X':
    cpu = 'O' # bedeutet weiß
    runCPU = False
    runPlayer = True
else:
    cpu = 'X' # bedeutet schwarz
    runCPU = True
    runPlayer = False
start = True

#theBoard = getTestBoard() # Testboard starten
theBoard = getNewBoard()
drawBoard(theBoard)

while True:
    if runCPU == False and runPlayer == True:
        spielerZieht(theBoard, start)
        start = False
        #cpuZieht(theBoard)
    if runCPU == True and runPlayer == False:
        cpuZieht(theBoard,cpu, start)
        #spielerZieht(theBoard)
        runCPU = False
        runPlayer = True
        start = False

