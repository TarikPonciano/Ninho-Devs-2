import time
import random
import os
while True:
    board = [
        [0 for i in range(40)] for j in range(40)
    ]

    for y in range(len(board)):
        for x in range(len(board[y])):
            
            if (random.randint(0,100) > 90):
                board[y][x] = 1
            else:
                board[y][x] = 0


    geracoes = 0

    while True:
        os.system("cls")
        
        print(f"------ GERAÇÃO {geracoes} ------")                                   
        
        for linha in board:
            row = ""

            for valor in linha:
                
                if valor == 0:
                    row += " ⬛ "
                else:
                    row += " ⬜ "

            print(row)
        
        for y in range(len(board)):
            for x in range(len(board[y])):
                vizinhos = 0
                for vizX in [-1, 0, 1]:
                    for vizY in [-1, 0, 1]:
                        if vizX == 0 and vizY == 0:
                            continue  # Pula a célula atual
                        
                        posX = x + vizX
                        posY = y + vizY
                        
                        if 0 <= posX < len(board[y]) and 0 <= posY < len(board):
                            if board[posY][posX] == 1:
                                vizinhos += 1

                if board[y][x] == 1:
                    if vizinhos < 2 or vizinhos > 3:
                        board[y][x] = 0  # Célula morre por solidão ou superpopulação
                    # Caso contrário, a célula continua viva
                else:
                    if vizinhos == 3:
                        board[y][x] = 1  # Célula nasce por reprodução

            
        
                
        
            
        geracoes += 1
        time.sleep(float(1/10))

