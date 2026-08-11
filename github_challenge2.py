n=int(input("Enter limit(positive integer)"))
if n>0:
    sum=0
    count=0
    for i in range(1,n+1):
        if i%2==0:
            count=count+1
            sum=sum+i
    print(f"sum of even numbers between 1 and {n} is {sum}")
    print(f"number of even numbers between 1 and {n} is {count}")
else:
    print("Enter a positive integer")