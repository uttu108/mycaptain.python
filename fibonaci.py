terms = int(input("terms you want :"))

n1, n2 = 0, 1
count = 0

if terms <= 0 :
    print("Enter a positive number :")
elif terms == 1 :
    print("Fibonaci sequence upto ",terms," :")
    print(n1)
else :
    print("Fibonaci sequence :")
    while count < terms :
        print(n1)
        nth = n1+n2
        n1=n2
        n2=nth
        count += 1
