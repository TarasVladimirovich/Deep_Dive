# 0
sq = [i for i in range(1, 101) if i % 2 and i % 3 and i % 5]
print(sq)
sq = [i for i in range(1, 101) if not i % 2 and not i % 3 and not i % 5]
print(sq)
sq = [i for i in range(1, 101) if i % 2 == 0 and i % 3 == 0 and i % 5 == 0]
print(sq)
sq = [i for i in range(1, 20) if i % 2 == 0]
print(sq)
sq = [i for i in range(1, 20) if not i % 2]
print(sq)
sq = [i for i in range(1, 20) if i % 2]
print(sq)
print(bool(0))
print(bool(2))
