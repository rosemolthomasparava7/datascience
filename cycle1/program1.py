a=int(input("enter lower limit"))
b=int(input("enter upper limit"))
for num in range(a,b+1):
  if num > 1:
    for i in range(2,num):
      if(num % i == 0):
          print(num)
          break
