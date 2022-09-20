start = int(input("Enter the starting point of range : "))
end = int(input("Enter the ending point of range : "))

for i in range(start,end+1):
    if i >= 0:
        print( i ,end=" ")
