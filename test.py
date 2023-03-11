with open('diff.txt', 'r') as f:
    for i in f:
        if '.txt' in i:
            print(i, end='')