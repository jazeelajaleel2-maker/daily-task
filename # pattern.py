# pattern.py


# for i in range(1,6):
#     print(i*"*")
# for i in range(5,0,-1):
#     print(i*"*")

# n=int(input("enter the number of lines:"))
# for i in range(1,n+i):
#     print(""*(n-i),i*"*")

# n=int(input("enter the number of lines:"))
# for i in range(1,n+1):
#     print(""*(n-i)+"*"*(2*i-1))

# n=int(input("enter the number of lines:"))
# for i in range(1,n+1):
#     print(""*(n-i)+"*"*(2*i-1))
# n=5
# for i in range(1,n+1):
#     print(" "*(n-i)+"*"*(2*i-1))

# n=5
# for i in range(n,0,-1):
#     print(" "*(n-i)+"*"*(2*i-1))

# for i in range(2,n+1):
#     print(" "*(n-i)+"*"*(2*i-1))  
# 
# 
#  

# n=10
# for i in range(1,n+1):
#     print(" "*(n-i)+"*"*(2*i-1))

# for i in range(n-1,0,-1):
#     print(" "*(n-i)+"*"*(2*i-1))




# i=10
# while i>0:
#     print(i)
#     i-=1






# i=1
# while i< 11:
#     print(i)
#     i+=1

# i=10
# while i>0:
#     print(i)
#     i-=1

# i=1
# while i<11:
#     print(i)
#     i+=1
# a="aswani"
# i=0
# rev=" "
# while i < len(a):
#     rev=a[i]+rev
#     i+=1
# print(rev)


# n=int(input("enter a number:"))
# i=1
# while i < n:
#     print(i)
#     i+=1

# n=int(input("enter a number:"))
# i=2
# while i < n:
#     if n%2==0:
#         print(i)
#         i+=2  


# n=int(input("enter a number:"))
# i=1
# sum=0
# while i<=n:
#     sum=sum+i
#     i=i+1
# print("sum of n numbers=",sum)

# n=int(input("enter a number:"))
# i=1
# whilen i <=10:
#     print(n,"x",i,"=",n*i)
#     i+=1

# n=int(input("enter a number:"))
# fact=1
# i=1
# while i<=n:
#     fact=fact*i
#     i=i+1
#     print(fact)

# n=int(input("enter a number:"))
# i=1
# count=0
# while i <=n:
#     if i % 3 ==0:
#         count=count+1
#     i = i+1
# print("count is",count)

# int(input("enter a number:"))
# i=1
# count=0
# while i <=n:
#     if i % 3 ==0:
#         count=count+1
#     i = i+1
# print("count is",count)

#
# n= int(input("enter a number:"))
# i=1
# sum = 0
# while i <=n:
#     if i % 2 == 0:
#         sum = sum + i
#     i = i+1
# print("sum is",sum)

# n= int(input("enter a number:"))
# i=1
# sum=0
# while i <=n:
#     sum=sum+i
#     i=i+1
# average = sum/n
# print("average is",average)

# n=int(input("enter a number:"))
# i=1
# while i <=n:
#     print(i*i)
#     i=i+1
# n=int(input("enter a number:"))
# i=1
# while i <=n:
#     print(i*i*i)
#     i=i+1

# n=int(input("enter a number:"))
# i=1
# count=0
# while i <=n: 
#     if i % 5 ==0:
#         count=count+1
#     i = i+1
# print("count is",count)

# n=int(input("enter a number:"))
# i=1
# count=0
# while i <=n: 
#     if i % 2 == 0 and i % 3 == 0:
#         count=count+1
#     i = i+1
# print("count is",count)



# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print( j, end =" ")
#     print()
    

# n=5
# for i in range(1,n+1):
#     for j in range (i):
#         print(i, end =" ")
#     print()

# n=5
# num=1
# for i in range(1,n+1):
#     for j in range(i):
#         print(num,end="")
#         num+=1
#     print()

# n=5
# for i in range(1,n+1):
#     for j in range(i,0,-1):
#         print(j,end="")
#     print()

n=5
for i in range(1,n+1):
    print(" "*(n-1),end="")
    for j in range(1,2*i):
        print(j,end="")
    print()



    # n=5
    # for i in range( 1, n+1 ):
    #     print(" " * (n-i), end= " " )
    #     for j in range(1, 2*i):
    #         print(j, end="")
    #     print()

    # for i in range( n-1, 0, -1):
    #     print( " " * (n-i), end= " ")                             
    #     for j in range(1, 2*i):
    #         print (j, end="" )
    #     print()


    # n=5
    # for i in range( n, 0,-1 ):
    #     print(" " * (n-i), end= " " )
    #     for j in range(1, 2*i):
    #         print(j, end="")
    #     print()

    # for i in range( 2, n+1 ):
    #     print( " " * (n-i), end= " ")                             
    #     for j in range(1, 2*i):
    #         print (j, end="" )
    #     print()






    # for i in range(1,11):
    #     if i==10:
    #         break
    #     print(i)



    # for i in range(1,11):
    #         if i%2==0:
    #             continue
    #         print(i)

    # for i in range(1,6):
    #         if i==3:
    #             pass
    #         print(i)



n=5
for i in range(n):
    for j in range(i + 1):
        print(chr(65 + i),end=" ")
    print()

