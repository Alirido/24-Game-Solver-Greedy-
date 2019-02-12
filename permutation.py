number = [3,4,2,3]
for i in range(0,4):
    for j in range(0,4):
        if (j != i):
            for k in range(0,4):
                if  (k!=j and k!=i):
                    for l in range(0,4):
                        if (k!=l and j!=l and i!=l):
                            print(number[i], number[j], number[k], number[l])