def f4(a_list):
    a_dic = {}
    for i in a_list:
        a_dic[i] = len(i)
    return a_dic

test = ['colorless', 'green', 'ideas', 'sleep', 'furiously']
print(f4(test))