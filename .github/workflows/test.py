with open('diff.txt', 'r') as f:
    soc=[]
    # d={}
    for i in f:
        if '.txt' in i:
             soc.append(i[:-1])
    print(soc)
    # print(','.join(soc))
    # d['version'] = s
    # print(s)
    # print(d)