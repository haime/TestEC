#!/usr/bin/python3
import sys
import os

class badminton(object):
    
    def __init__(self,P1,P2):
        self.players=[P1,P2]        
        self.score=[0,0]
        self.setPlayers=[0,0]
        self.setNumber=1
        self.endGame=False

    def winSet(self):
        
        if self.score[0]>= 21 or self.score[1]>= 21:
            setadv= 'Set para el jugador '
            if self.score[0]-self.score[1] >= 2 or self.score[0]== 30:
                self.setPlayers[0]+=1
                setadv +=self.players[0]
                self.score=[0,0]
                self.winGame()
                if not self.endGame:    
                    print(setadv+', cambio de cancha.' )
                    if self.setNumber == 2:
                        print('MATCH') 
                    print('Presiona cualquier tecla para continuar ...')                    
                self.setNumber+=1

            elif self.score[1]-self.score[0] >= 2 or self.score[0]== 30:
                self.setPlayers[1]+=1
                setadv +=self.players[1]
                self.score=[0,0]
                self.winGame()
                if not self.endGame:
                    print(setadv+', cambio de cancha.' )
                    if self.setNumber == 2:
                        print('MATCH')
                    print('Presiona cualquier tecla para continuar ...')
                self.setNumber+=1
                

    def winGame(self):
        if self.setPlayers[0] == 2:
            self.endGame = True
            self.printGame()
            print('El Jugador '+self.players[0]+' es le ganador')
            #sys.exit()           
        elif self.setPlayers[1] == 2:
            self.endGame = True
            self.printGame()
            print('El Jugador '+self.players[1]+' es le ganador')
            #sys.exit()
    
    def waitPoint(self):
        point = input()
        if point == 'q':
            self.addPoint(0)
        elif point == 'p':
            self.addPoint(1)

    def addPoint(self,player):
        self.score[player]+=1

    def addSet(self,player):
        self.setPlayers[player]+=1

    def printGame(self):
        print (' '*4+self.players[0][0:5]+' '*4+'Jugador'+' '*4+self.players[1][0:5])
        print (' '*6+str(self.setPlayers[0])+' '*6+'SetWin '+' '*6+str(self.setPlayers[1]))
        print (' '*6+str(self.score[0])+' '*6+' Score '+' '*6+str(self.score[1]))
        print ('\n'*3 )
    
    def play(self):
        
        while not self.endGame:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.printGame()
            self.winSet()
            self.waitPoint()   
        
        





def main():
    b=badminton('Guadalupe','Alan')
    b.play()



if __name__ == '__main__':
    main()