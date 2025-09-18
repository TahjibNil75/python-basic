

for token in range (1, 11):
    print(f"Token number {token} dispensed.")


print("----------------------------------------------")


players = ["player1", "player2", "player3", "player4", "player5"]

for name in players:
    print(f"{name} is ready to play!")


print("----------------------------------------------")



for index, name in enumerate(players, start=1):
    print(f"{index}: {name} is ready to play!")
