for i in range(1,5):
    for j in range(1,5):
        print(j,end=' ')

    print()


nested_list = [[j for j in range(1,5)] for i in range(1,5)]
print(nested_list)


mul = [[i*j for j in range(1,5)] for i in range(1,5)]
print(mul)

fMap = [item for sublist in mul for item in sublist]
print(fMap)