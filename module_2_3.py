numbers = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
quantity =  len(numbers)
a = 0
while a < quantity:
    if numbers [a] == 0:
        a = a + 1
        continue
    elif numbers [a] > 0:
        print(numbers[a])
        a = a + 1
    elif numbers [a] < 0:
        break