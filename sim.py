
import random as rand
import json


names = ["jeff", "john", "jim", "jerry", "josh"]

def makePlayers():
    
    players = {}

    for i in range(5):
        players[names[i]] = rand.randint(70, 90)

    return players

class Team:

    def __init__(self, name):
        self.name = name
        self.players = makePlayers()

def decideOutcome(t1, t2):
    team1sum = 0
    team2sum = 0

    for rating in t1.players.values():
        team1sum += rating
    for rating in t2.players.values():
        team2sum += rating
    
    if team1sum > team2sum:
        return t1.name
    elif team1sum == team2sum:
        coinflip = rand.randint(1,2)
        if coinflip == 1:
            return t1.name
        else:
            return t2.name
    else:
        return t2.name
    
def play(team1, team2):
    print("-------------------------")
    print(f"The match between the {team1.name} and the {team2.name} now begins!")
    print()
    print(f"The {team1.name}: {team1.players}")
    print(f"The {team2.name}: {team2.players}")
    winner = decideOutcome(team1, team2)
    print()
    print(f"The {winner} have won the match!")
    print("-------------------------")
    
def read_player_data(path):
    with open(path, "r") as file:
        data = json.load(file)
    return data
    

def main():

    mice = Team("Mice")
    snakes = Team("Snakes")

    play(mice, snakes)

# main()

mydata = read_player_data("players.json")
print(mydata[0]["overall"])