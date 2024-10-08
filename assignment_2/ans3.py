def f3(a_set):
    divisible_by_7 = set()  # new set for storing
    for i in a_set:
        if i % 7 == 0:
            divisible_by_7.add(i) 
    return len(divisible_by_7)

numbers_below_1000 = set(range(1000))

print(f3(numbers_below_1000))