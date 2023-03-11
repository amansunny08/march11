with open('diff.txt', 'r') as f:
    soc=[]
    for i in f:
        if '.txt' in i:
             soc.append(i[:-1])
    # print(soc)
    print(','.join(soc))