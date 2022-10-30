def kam(jewels, stone):
    count_jewels = 0
    for i in jewels:
        if i in stone:
            count_jewels += stone.count(i)
    return count_jewels

jewels = int(input("jewels: "))
stone = int(input("stone: "))
print(kam(jewels, stone))