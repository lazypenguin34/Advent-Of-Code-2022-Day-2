#Getting data
with open("input.txt", "r") as file:
  rounds = [i for i in file.read().strip().split("\n")]

#Mapping each possibility to a score
scoreP1 = {"A X":4, "A Y":8, "A Z":3, "B X":1, "B Y":5, "B Z":9, "C X":7, "C Y":2, "C Z": 6}

#For every round of RPS in the strategy guide, add the amount of points to the player that correspond with the round's outcome given in the dictionary above
playerPointsP1 = 0
for round in rounds:
  playerPointsP1 += scoreP1[round]

#Print results
print(playerPointsP1)

#Mapping each possibilty to the new scores that arise with the different rules
scoreP2 = {"A X":3, "A Y":4, "A Z":8, "B X":1, "B Y":5, "B Z":9, "C X":2, "C Y":6, "C Z": 7}

#Same process as before here, but now we are using the new outcomes defined above
playerPointsP2 = 0
for round in rounds:
  playerPointsP2 += scoreP2[round]

#Print results
print(playerPointsP2)