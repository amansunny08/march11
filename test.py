with open('diff.txt', 'r') as f:
    for i in f:
        if '.py' in i:
            print(i, end='')