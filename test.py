alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

BETA =   dict(zip(alphabet, "LEYJVCNIXWPBQMDRTAKZGFUHOS"))

CONVERSION_TOL = dict(zip([i for i in range(26)], alphabet))
CONVERSION_TOI = dict(zip(alphabet, [i for i in range(26)]))

print(CONVERSION_TOI)
print(CONVERSION_TOL)