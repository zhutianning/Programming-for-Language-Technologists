def divisible_13(number):
    their_sum = 0
    i_count = 0
    for i in range(1,int(number)+1):
        if i % 13 == 0:
            i_count += 1
            their_sum += i
    return (i_count,their_sum)

test = int(1000000)
print(divisible_13(test))