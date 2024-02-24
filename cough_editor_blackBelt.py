import json
import os

def main():
    keepGoing = True
    game = None
    while keepGoing:
        userChoice = getMenuChoice()
        userChoice = int(userChoice)
        if userChoice == 0:
            keepGoing = False
            print("Thank you for playing!")
        elif userChoice == 1:
            print("Loading default game")
            game = getDefaultGame()
        elif userChoice == 2:
            game = loadGame()
        elif userChoice == 3:
            saveGame(game)
        elif userChoice == 4:
            if game is not None:
                editNode(game)
            else:
                print("Please load a game first.")
        elif userChoice == 5:
            if game is not None:
                playGame(game)
            else:
                print("Please load a game first.")

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
        "start": {
            "description": "You are in a dark room",
            "menus": ["Play Again", "Exit"],
            "nodes": ["start", "quit"]
        }
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
    try:
        nodeData = game[currentNode]
        description = nodeData["description"]
        menus = nodeData["menus"]
        nodes = nodeData["nodes"]
        
        print(f"{description}")
        for i, menu in enumerate(menus, start=1):
            print(f"{i}) {menu}")
            
        while True:
            response = input("What will you do? (Enter the number of your choice) ")
            if response.isdigit():
                response = int(response)
                if response >= 1 and response <= len(nodes):
                    nextNode = nodes[response - 1]
                    break
                else:
                    print("Invalid choice. Please select a valid option.")
            else:
                print("Invalid input. Please enter a number.")
        return nextNode
    except KeyError:
        print("Illegal node encountered. Exiting the game.")
        return "quit"

def saveGame(game):
    try:
        filename = input("Enter the filename to save (must end with .json): ")
        if not filename.endswith('.json'):
            print("File name must end with .json extension.")
            return
        with open(filename, "w") as outFile:
            json.dump(game, outFile, indent=2)
        print(f"Saved game data to {filename}")
    except Exception as e:
        print(f"Error occurred while saving the game: {e}")

def loadGame():
    try:
        files = os.listdir()
        print("Available game files:")
        for file in files:
            if file.endswith(".json"):
                print(file)
        filename = input("Enter the filename to load: ")
        with open(filename, "r") as inFile:
            game = json.load(inFile)
        print(f"Loaded game from {filename}")
        return game
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"Error occurred while loading the game: {e}")
    return None

def editNode(game):
    try:
        print("Current status of game:")
        print(json.dumps(game, indent=2))
        print("Current Nodes:")
        for nodeName in game.keys():
            print(nodeName)

        newNode = input("Name of new node? ")
        if newNode in game.keys():
            print("Node already exists. Editing existing node.")
            nodeData = game[newNode]
        else:
            print("Creating new node.")
            nodeData = {"description": "", "menus": [], "nodes": []}

        nodeData["description"] = input("Enter the description for this node: ")
        numMenus = int(input("How many menus do you want for this node? "))
        for i in range(numMenus):
            menu = input(f"Enter menu option {i + 1}: ")
            nodeData["menus"].append(menu)

        print("For each menu option, enter the corresponding node name:")
        for menu in nodeData["menus"]:
            node = input(f"Enter the node for menu option '{menu}': ")
            nodeData["nodes"].append(node)

        game[newNode] = nodeData
        print("Node updated successfully.")
    except Exception as e:
        print(f"Error occurred while editing node: {e}")

if __name__ == "__main__":
    main()