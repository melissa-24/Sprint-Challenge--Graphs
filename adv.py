from room import Room
from player import Player
from world import World
from util import Stack

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

#keep track of "reverse directions" so we can keep track of valid moves
backtrack = []
rev_direct = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

#set so we can track visited rooms
# paths = Stack()
visited = set()

#while we have rooms that are unvisited

#initial test
while len(visited) < len(room_graph):
    next_move = None
    #for each exit in the room
    for exit in player.current_room.get_exits():
        if player.current_room.get_room_in_direction(exit) not in visited:
            next_move = exit
            break
    if next_move is not None:
        traversal_path.append(next_move)
        backtrack.append(rev_direct[next_move])
        player.travel(next_move)
        visited.add(player.current_room)
    else:
        next_move = backtrack.pop()
        traversal_path.append(next_move)
        player.travel(next_move)

#new test
# while len(visited) < len(world.rooms):
#     exits = player.current_room.get_exits()
#     path = []

#     for exit in exits:
#         if exit is not None and player.current_room.get_room_in_direction(
#             exit) not in visited:
#             path.append(exit)

#     visited.add(player.current_room)

#     if len(path) > 0:
#         move = random.randint(0, len(path) - 1)
#         paths.push(path[move])
#         player.travel(path[move])
#         traversal_path.append(path[move])
#         print(f'Avail Paths: {path}, Direction: {path[move]}')
#     else:
#         move_back = paths.pop()
#         player.travel(rev_direct[move_back])
#         traversal_path.append(rev_direct[move_back])
#         print(move_back, "Going to previous room")



# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")