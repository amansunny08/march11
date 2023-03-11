with open('diff.txt', 'r') as f:
    soc=[]
    for i in f:
        if '.py' in i:
             soc.append(i[:-1])
    # print(soc)
    print(','.join(soc))