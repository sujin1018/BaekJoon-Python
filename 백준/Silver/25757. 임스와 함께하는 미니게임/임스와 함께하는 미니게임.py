import sys
input = sys.stdin.readline
num, game = input().split()
player=set()
gameType = {"Y":1, "F":2, "O":3}
for _ in range(int(num)):
    player.add(input())
print(len(player)//gameType.get(game))