def most_frequent(string) :
    u = dict()
    for i in string :
        if i not in u :
            u[i]= 1
        else :
            u[i] += 1
    return u

print(most_frequent('Mississippi'))
