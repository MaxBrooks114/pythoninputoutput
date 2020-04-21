import shelve

games = shelve.open("game")

loc = 1
while True:
    available_exits = ", ".join(games["locations"][loc]["exits"].keys())
    print(games["locations"][loc]["desc"])

    if loc == 0:
        break
    else:
        all_exits = games["locations"][loc]["exits"].copy()
        all_exits.update(games["locations"][loc]["named_exits"])
    direction = input("Available exits are " + available_exits + " ").upper()
    print()

    if len(direction):
        words = direction.split()
        for word in words:
            if word in games["vocab"]:
                direction = games["vocab"][word]
                break
        # for word in words:
        #     if word in direction:
        #         direction = words[word]
    if direction in all_exits:
        loc = all_exits[direction]
    else:
        print("you cannot go in that direction")