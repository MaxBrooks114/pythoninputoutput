import shelve


games = shelve.open("game")
games["locations"] = {
    0:{"desc": "computer", "exits": {}, "named_exits": {}},
    1:{"desc": "road", "exits": {'W': 2, "E": 3, "N": 5, "S": 4, "Q": 0}, "named_exits": {"2": 2, "3": 3, "5": 5, "4": 4 }},
    2:{"desc":  "hill","exits": {"N":5, "Q": 0}, "named_exits": {"5": 5}},
    3:{"desc":  "building","exits": {"W": 1, "Q":0}, "named_exits": {"1": 1}},
    4:{"desc":  "valley","exits": {"N":1, "W":2, "Q": 0}, "named_exits": {"1":1, "2": 2}},
    5:{"desc":  "forest", "exits":{"W": 2, "S":1, "Q": 0}, "named_exits": {"2": 2, "1": 1}}
}
games["vocab"] = { "QUIT": "Q", "NORTH": "N", "SOUTH": "S", "EAST": "E", "WEST": "W", "ROAD": "1", "HILL": "2", "BUILDING": "3", "VALLEY": "4", "FOREST": "5"}



print(games["locations"])

games.close()