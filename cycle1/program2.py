n=int(input("how many no.of terms : "))
n1,n2=0,1
i=0
if n < 0:
    print("enter positive number :")
elif n == 1:
    print("fibonacci sequence:",n1)
else:

    print("fibonacci sequence")
    while i < n:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        i += 1