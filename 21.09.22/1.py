game_list = []
name_game=input()
while name_game !=0:
    if name_game in game_list:
        print("Эта игра уже записана")
    else:
        game_list.append(name_game)
    name_game=input()
game_list.sort()
print(game_list)
game_list