def f5(x1,x2):
    run_times = 0
    while x1 < x2:
        x1 = x1 * 3
        x2 = x2 - 2
        run_times += 1
    return run_times

def g(y1):
    a_dict = {}
    for y in range(0,y1):
        a_dict[y] = f5(y, y ** 2)    
    return a_dict

def main():
    test = g(20)
    print(test)

main()