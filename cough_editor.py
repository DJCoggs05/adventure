# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 10:19:46 2024

@author: cough
"""
import json

def main():
    keepGoing = True
    while keepGoing:
        userChoice = getMenuChoice()
        userChoice = int(userChoice)
        if userChoice == 0:
            keepGoing = False
            print("Thank you for playing!")
        if userChoice == 1:
            print("Loading Default Game")
            game = getDefaultGame()
            
        #elif userChoice == 2:
        
        elif userChoice == 3:
            saveGame(game)
        #elif userChoice == 4:
            
        elif userChoice == 5:
            playGame(game)
def getMenuChoice():
    print("""
0) exit
1) load default game
2) load a game file
3) save the current game
4) edit or add a node
5) play the current game    
""")
    userChoice = input("What would you like to do? ")
    
    return userChoice

def getDefaultGame():
    game = {
 "start": ["You are in a dark room", "Play Again", "start", "Exit", "quit"]
}
    return game
def playGame(game):
    keepGoing = True
    currentNode = "start"
    while keepGoing:
    	if currentNode == "quit":
            keepGoing = False
    	else:
    		currentNode = playNode(game, currentNode)

def playNode(game, currentNode):
    if currentNode in game.keys():
        (description, menuA, nodeA, menuB, nodeB) = game[currentNode]
        print(f"""
{description}
1) {menuA}
2) {menuB}""")
    response = input("What will you do? (1/2) ")
    if response == "1":
        nextNode = nodeA
    if response == "2":
        nextNode = nodeB
    else:
        print("Please select 1 or 2")
    return nextNode

def saveGame(game):
    outFile = open("game.json", "w")
    json.dump(game, outFile, indent=2)
    outFile.close()
    print("saved game data to game.json")


main()