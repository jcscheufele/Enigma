rotations = 1
rotations_1 = 1
rotations_2 = 1
for i in range(100):
    rotations_1 = ((rotations_1 + 1) % 26)
    rotations_2 = ((rotations_2 + 1) % 26)
    print(rotations_1, rotations_2+1)