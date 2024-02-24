# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 10:19:46 2024

@author: cough
"""
import json

def main():
    keepGoing = True
    game = None
    while keepGoing:
        userChoice = getMenuChoice()
        userChoice = int(userChoice)
        if userChoice == 0:
            keepGoing = False
            print("Thank you for playing!")
        if userChoice == 1:
            print("Loaded Default Game")
            game = getDefaultGame()
        elif userChoice == 2:
            game = loadGame()
        elif userChoice == 3:
            saveGame(game)
        elif userChoice == 4:
            if game != None:
                editNode(game)
            else:
                print("Please load a game first.")
        elif userChoice == 5:
            playGame(game)
            
def getMenuChoice():
    print("""
0) Exit
1) Load default game
2) Load a game file
3) Save the current game
4) Edit or add a node
5) Play the current game    
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
    print("Saved game data to game.json")
    print(f"""Your game contains:
          {game}""")

def loadGame():
    inFile = open("game.json", "r")
    game = json.load(inFile)
    print(f"""Loaded 'game':
Game Contents:
{game}""")
    inFile.close()
    
    return game


def editNode(game):
    print("Current status of game:")
    print(json.dumps(game, indent = 2))
    print ("Current Nodes:")
    for nodeName in game.keys():
        print(nodeName)
        
    newNode = input("Name of new node?")
    if newNode in game.keys():
        newSection = game[newNode]
    else:
        newSection = ["", "", "", "", ""]
    (description, menuA, nodeA, menuB, nodeB) = newSection
    
    newDescription = editField("description", description)
    newMenuA = editField("Menu A", menuA)
    newNodeA = editField("Node A", nodeA)
    newMenuB = editField("Menu B", menuB)
    newNodeB = editField("Node B", nodeB)

    game[newNode] = [newDescription, newMenuA, newNodeA, newMenuB, newNodeB]
    
def editField(fieldName, currentValue):
    newValue = input(f"Enter new value for {fieldName} (Press Enter to keep current value {currentValue}): ")
    if newValue.strip():
        return newValue
    else:
        return currentValue

main()