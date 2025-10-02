"""
output example:

=== Summary ===
Players: 2
Highest: Alice - 95
Lowest: Cara - 88
Average: 91.5

"""

# Output player summary
print("===Summary===")
print(f"Players: {None}")
print(f"Highest: {None}")
print(f"Lowest: {None}")
print(f"Average: {None}")

# main.py

# 假設有兩位玩家
players = [
    ("Alice", 95),
    ("Cara", 88)
]

# 計算玩家數量
num_players = len(players)

# 找最高分與最低分
highest = max(players, key=lambda x: x[1])
lowest = min(players, key=lambda x: x[1])

# 計算平均分
average = sum(score for _, score in players) / num_players

# 顯示統計資訊

players = [("kk", 55),("rr", 55),("oo", 55)]
hight_corse_player = (None,0 )
lowest_corse_player = (None,0 )
sverage = 0

print("== Summary ==")
print(f"Players: {num_players}")
print(f"Highest: {highest[0]} - {highest[1]}")
print(f"Lowest: {lowest[0]} - {lowest[1]}")
print(f"Average: {average}")

