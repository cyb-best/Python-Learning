for number in range(1, 21):
    print(number)

digits = list(range(1, 1_000_001))
print(digits)
print(sum(digits))

digits1 = list(range(1, 21, 2))
for digit in digits1:
    print(digit)

digits2 = list(range(3, 31, 3))
print(digits2)


digits3 = []
for digit in range(1, 11):
    digits3.append(digit ** 3)
print(digits3)

digits4 = [number ** 3 for number in range(1, 11)]
print(digits4)